from webbrowser import open_new_tab
from jinja2 import Environment, FileSystemLoader


def get_word_font_list(freq_dict):
    min_fontsize, max_fontsize = 12, 30
    max_tag_freq = max(freq_dict.values())
    word_font_list = []

    for key, value in freq_dict.items():
        font_size = int((value / float(max_tag_freq)) *
                        (max_fontsize - min_fontsize) + min_fontsize)
        word_font_list.append((key, font_size))
    return word_font_list


def create_tag_cloud():
    freq_dict = {'dummy': 5, 'search': 7, 'word': 4, 'words': 3, 'text': 2, 'number': 1, 'will': 1, 'frequency': 1, 'file': 1, 'print': 1, 'line': 2, 'didnt': 1}

    word_font_list = get_word_font_list(freq_dict)
    word_font_list = {'words': (15, ['this is ling text line1', 'line2', 'line3']),'dummy': (19, ['line4', 'line6', 'line9'])}
    HTML = """
    {% extends "base.html" %}
    {% block body %}
      <ul style="list-style: none;">
      {% for word in word_font_list %}
        <li style="display: inline;">
            <a onclick="showDetails(this)" data-linelist='{{word_font_list[word][1]|tojson|safe}}' style="font-size:{{word_font_list[word][0]}}px;">{{word}}</a>
        </li>
      {% endfor %}
      </ul>

    {% endblock %}
    """
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.from_string(HTML).render(word_font_list=word_font_list)
    print template
    tagcloud_template_path = 'templates/tagcloud.html'

    with open(tagcloud_template_path, 'w') as f:
        f.write(template)
    open_new_tab(tagcloud_template_path)

if __name__ == '__main__':
    create_tag_cloud()
