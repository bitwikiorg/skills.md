package main
 import (
 "encoding/json"
 "fmt"
 "os"
 "path/filepath"
 "strings"
 )

 type Skill struct {
 ID string `json:"id"`
 Path string `json:"path"`
 Provider string `json:"provider"`
 }

 func main() {
 var skills []Skill
 err := filepath.Walk("sources", func(path string, info os.FileInfo, err error) error {
 if !info.IsDir() && strings.HasSuffix(path, ".js") {
 parts := strings.Split(path, string(os.PathSeparator))
 if len(parts) >= 3 {
 provider := parts[1]
 name := strings.TrimSuffix(parts[len(parts)-1], ".js")
 id := provider + "." + name
 skills = append(skills, Skill{ID: id, Path: path, Provider: provider})
 }
 }
 return nil
 })
 if err != nil { panic(err) }

 jsonData, _ := json.MarshalIndent(skills, "", " ")
 const SHARD_THRESHOLD = 5 * 1024 * 1024 // 5MB
 os.MkdirAll("swarm/index", 0755)

 if len(jsonData) > SHARD_THRESHOLD {
 fmt.Println("Index > 5MB. Sharding by provider...")
 byProvider := make(map[string][]Skill)
 for _, s := range skills {
 byProvider[s.Provider] = append(byProvider[s.Provider], s)
 }
 manifest := make(map[string]string)
 for p, sList := range byProvider {
 shardData, _ := json.MarshalIndent(sList, "", " ")
 fname := fmt.Sprintf("swarm/index/%s.json", p)
 os.WriteFile(fname, shardData, 0644)
 manifest[p] = fname
 }
 manifestData, _ := json.MarshalIndent(manifest, "", " ")
 os.WriteFile("swarm/index/master.json", manifestData, 0644)
 os.WriteFile("swarm/index.json", jsonData, 0644)
 } else {
 fmt.Println("Index < 5MB. Writing monolithic index.")
 os.WriteFile("swarm/index.json", jsonData, 0644)
 }
 fmt.Println("Index generated.")
 }
