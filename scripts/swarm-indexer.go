package main
import (
    "fmt"
    "os"
    "path/filepath"
    "strings"
    "encoding/json"
)
type Skill struct {
    ID   string `json:"id"`
    Path string `json:"path"`
}
func main() {
    var skills []Skill
    err := filepath.Walk("sources", func(path string, info os.FileInfo, err error) error {
        if !info.IsDir() && strings.HasSuffix(path, ".js") {
            // Minimal parsing to get ID would be better, but for now just index the path
            skills = append(skills, Skill{ID: filepath.Base(path), Path: path})
        }
        return nil
    })
    if err != nil { panic(err) }
    jsonData, _ := json.MarshalIndent(skills, "", "  ")
    os.MkdirAll("swarm", 0755)
    os.WriteFile("swarm/index.json", jsonData, 0644)
    fmt.Println("Index generated.")
}
