
import os
import json
from fastembed import TextEmbedding

# Initialize model (lightweight)
print("Loading model...")
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

skills = []
texts = []
ids = []

print("Scanning skills...")
for root, dirs, files in os.walk("sources"):
    for file in files:
        if file.endswith(".js"):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                content = f.read()
            # Simple extraction: Use the whole content for now, or split frontmatter
            # Ideally we embed the description + ID. For MVP, embed the whole file content (truncated if needed)
            texts.append(content[:8192]) # Limit context window
            ids.append(file)

if not texts:
    print("No skills found.")
    exit(0)

print(f"Generating embeddings for {len(texts)} skills...")
embeddings = list(model.embed(texts))

output = {}
for i, skill_id in enumerate(ids):
    output[skill_id] = [float(x) for x in embeddings[i]]

os.makedirs("swarm", exist_ok=True)
with open("swarm/embeddings.json", "w") as f:
    json.dump(output, f)

print("Embeddings saved to swarm/embeddings.json")
