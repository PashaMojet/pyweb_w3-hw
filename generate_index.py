#%%
import datetime
import generate_hor

def generate_index(horoscopes,name_page = "defaul_name"):
    date = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d")
    h1 = f"<h1>Твой прогноз на {date}</h1>"
    p =''
    for i in horoscopes:
       p = p + f"<p>{i}</p>\n"
    header = f"""<html>
    <head>
    <meta charset = 'utf-8'>
    <title>{name_page}</title>
    </head>
    <body>
    {h1}
    {p}
    <hr/>
    <p><a href = 'about.html'>О реализации</a></p>
    </body>
    </html>"""
    with open("index.html","w",encoding="utf8") as index:
        print(header,file=index)
    return 1
def gen_about(horoscopes,name_page = "О реализации",picture = "w960.jpg"):

    header = f"""
    <head>
    <meta charset = 'utf-8'>
    <title>{name_page}</title>
    </head>
    """
    time = []
    verbs = []
    other = []
    for i in horoscopes:
        if i.split()[0] not in time:
            time.append(i.split()[0])
        if i.split()[1] not in verbs:
            verbs.append(i.split()[1])
        if i.split()[2] not in other:
            other.append(i.split()[2])
    ol_verb = '<ol><li>Глаголы:</li>\n'
    ul_verb = ''
    for i in verbs:
      ul_verb += f"<li>{i.title()}</li>\n"
    ol_verb = ol_verb + f"<ul>{ul_verb}</ul>"

    ol_time = '<li>Время:</li>\n'
    ul_time = ''
    for i in time:
      ul_time += f"<li>{i.title()}</li>\n"
    ol_time = ol_time + f"<ul>{ul_time}</ul>"
    
    ol_other = '<li>Ожидания:</li>\n'
    ul_other = ''
    for i in other:
      ul_other += f"<li>{i.title()}</li>\n"
    ol_other = ol_other + f"<ul>{ul_other}</ul>"

    ol_verb = ol_verb + ol_time + ol_other + '</ol>'     

    body = f"""
    <body>
    <h1>О чем все это</h1>
    <img  width='100' weight = '100' src='w960.jpg'>
    {ol_verb}
    </body>
    """
    html = f"""<html>
    {header}
    {body}
    <p><a href ='index.html'>На главную</a><p>
    </html>
    """
    with open("about.html","w",encoding="utf8") as ab:
        print(html,file=ab)

lst_hor = gen_hor(4)
generate_html(horoscopes = lst_hor,name_page = "Гороскоп" )
gen_about(horoscopes = lst_hor)
# %%

