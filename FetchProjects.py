from bs4 import BeautifulSoup
import requests


def fetchProjects(pagenum):
    html_text = requests.get("https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3&page="+pagenum).text
    soup = BeautifulSoup(html_text, 'lxml')
    return soup.find_all('a', class_='package-snippet')


def getProjectLinkAndName(project):
    start_path = 'https://pypi.org/'
    name = project['href'][1:len(project['href'])-1].split('/')[-1]
    return name, start_path+project['href']


def getProjectRepoLink(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    project_repo_link = soup.find('a', class_='vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed')
    if project_repo_link is not None:
        return project_repo_link['href']
    else:
        return None


def cloneRepository(repolink):
    pass


if __name__ == '__main__':
    for i in range(500):
        all_projects = fetchProjects(str(i+1))
        for project in all_projects:
            project_name, project_link = getProjectLinkAndName(project)
            repository_link = getProjectRepoLink(project_link)
            # print(repository_link)
            if repository_link is not None:
                # print(project_name)
                # print(repository_link)
                filename = 'projects/'+project_name
                with open(filename, 'w') as fname:
                    fname.write(repository_link)
                    fname.close()




