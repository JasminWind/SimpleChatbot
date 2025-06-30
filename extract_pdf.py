import PyPDF2

def extract_text_from_pdf(pdf_path, output_txt_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"

    with open(output_txt_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

    print(f"Text extracted and saved to {output_txt_path}")

# Example usage
extract_text_from_pdf("example.pdf", "output.txt")
