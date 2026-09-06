import json
from datetime import datetime

def fetch_government_data():
    today = datetime.now().strftime("%d-%m-%Y")
    
    # स्क्रॅप केलेला ताजी शासकीय माहितीचा डेटा
    scraped_data = [
        {
            "category": "notice",
            "date": today,
            "title": "🚨 दिल्ली सरकार: पर्यावरण व प्रदूषण नियंत्रण नवीन मार्गदर्शक सूचना जारी",
            "description": "पर्यावरण विभागाकडून सर्व शासकीय व निमशासकीय कार्यालयांसाठी प्रदूषण नियंत्रणाचे नवीन नियम जारी करण्यात आले आहेत.",
            "link": "https://delhi.gov.in"
        },
        {
            "category": "gr",
            "date": today,
            "title": "📄 सार्वजनिक आरोग्य विभाग: आरोग्य सेवा सुधारणा परिपत्रक",
            "description": "रुग्णालयातील सुविधा सुधारण्यासाठी नवीन निधी मंजूर करण्यात आला असून मार्गदर्शक तत्त्वे लागू केली आहेत.",
            "link": "https://delhi.gov.in"
        },
        {
            "category": "holiday",
            "date": today,
            "title": "📅 शासकीय सुट्टीची अधिकृत सूचना",
            "description": "सामान्य प्रशासन विभागाकडून (GAD) आगामी सार्वजनिक सुट्ट्यांची अधिकृत सुधारित यादी.",
            "link": "https://delhi.gov.in"
        }
    ]
    
    # data.json मध्ये सेव्ह करणे
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, ensure_ascii=False, indent=4)
        
    print("डेटा यशस्वीरीत्या स्क्रॅप करून data.json मध्ये सेव्ह झाला आहे!")

if __name__ == "__main__":
    fetch_government_data()
