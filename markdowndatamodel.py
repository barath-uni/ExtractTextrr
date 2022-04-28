
class MarkdowndataModel(object):
    def __init__(self):
        super().__init__()
        self.title = 'My first post'
        self.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        self.date = '2020-02-02'
        self.modified_date = '2020-02-02'
        self.image = "/assets/images/posts/random-img.jpg"

    def get_model_info_as_text(self):
        text = "---\n"
        text += f"title: '{self.title}'\n"
        text += f"description: '{self.description}'\n"
        text += f"date: '{self.date}'\n"
        text += f"modified_date: '{self.modified_date}'\n"
        text += f"image: '{self.image}'\n"
        text += "---\n"
        return text

    def set_model_info(self, title, description, date, modified_date, image):
        self.title = title
        self.description = description
        self.date = date
        self.modified_date = modified_date
        self.image = image

