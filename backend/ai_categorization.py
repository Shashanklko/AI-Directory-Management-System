import torch
import torchvision.transforms as transforms
from PIL import Image
from transformers import BertTokenizer, BertForSequenceClassification

# Load Text Categorization Model (BERT)
class TextCategorizer:
    def __init__(self, model_path):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.model.to(self.device)
        self.model.eval()

    def categorize(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        outputs = self.model(**inputs)
        category = torch.argmax(outputs.logits).item()
        return category  # Map this to actual category labels


# Load Image Categorization Model (ResNet/MobileNet)
class ImageCategorizer:
    def __init__(self, model_path):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = torch.jit.load(model_path).to(self.device)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

    def categorize(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image = self.transform(image).unsqueeze(0).to(self.device)
        output = self.model(image)
        category = torch.argmax(output).item()
        return category  # Map this to actual category labels
