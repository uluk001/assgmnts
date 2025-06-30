class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class ReportGenerator:
    def __init__(self, report):
        self.report = report

    def generate_pdf(self):
        print("PDF generated")


class ReportSaver:
    def __init__(self, report):
        self.report = report

    def save_to_file(self, filename):
        print(f"Saved {filename}")
