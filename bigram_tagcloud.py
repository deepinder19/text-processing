from webbrowser import open_new_tab
from jinja2 import Environment, FileSystemLoader
from bigram_freq import bigram_freq2


def get_word_font_list(freq_dict, file_path):
    
    min_fontsize, max_fontsize = 12, 30
    max_tag_freq = max(freq_dict.values())
    word_font_dict = {}

    for key, value in freq_dict.items():
        font_size = int((value / float(max_tag_freq)) *
                        (max_fontsize - min_fontsize) + min_fontsize)
        word_font_dict[key] = (font_size, [])
    
    with open(file_path, 'r') as f_obj:
        for line in f_obj:
            for key, value in word_font_dict.items():
                if key[0] in line.lower() and key[1] in line.lower():
                     word_font_dict[key][1].append(line)
    return word_font_dict


def create_tag_cloud():
    """
    Problem 7
    
    This function displays in html tag cloud of bigram words read from file
    and lines in which it appears
    """
    
    freq_dict = bigram_freq2('demo.txt', 'noise_words.txt')
    word_font_list = get_word_font_list(freq_dict, 'demo.txt')
    HTML = """
    {% extends "base.html" %}
    {% block body %}
      <ul style="list-style: none;">
      {% for word in word_font_list %}
        <li style="display: inline;">
            <a onclick="showDetails(this)" data-linelist='{{word_font_list[word][1]|tojson|safe}}' style="font-size:{{word_font_list[word][0]}}px;">{{word[0]}}{{word[1]}}</a>
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
