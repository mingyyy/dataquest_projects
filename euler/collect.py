from requests_html import HTMLSession

# Collect Euler projects

for number_of_prob in range(20, 100):
    url = f"https://projecteuler.net/problem={number_of_prob}"
    session = HTMLSession()
    page = session.get(url)

    title = page.html.find('#content > h2', first=True)
    file_name = "Problem_" + str(number_of_prob) + "-" + str(title.text).replace(" ", "_") + ".py"
    print(file_name)

    with open(file_name, "w") as f:
        content = page.html.find('div.problem_content > p', first=False)
        f.write('""" \n')
        for c in content:
            f.write(c.text + "\n")
        f.write('"""')
