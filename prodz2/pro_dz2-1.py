import json

class CountryFinder:
    def __init__(self, jsonfile):
        with open(jsonfile, 'rb') as fp:
            countries_dict = json.load(fp)
        self.iter_dict = iter(countries_dict)

    def __iter__(self):
        return self

    def __next__(self):
        country_data = next(self.iter_dict)

        return country_data

    def put_wiki_urls(self, file_path):
        with open(file_path, 'wb') as f:
            for i in self:
                name = i['name']['common']
                url = 'https://en.wikipedia.org/wiki/' + name.replace(' ', '_')
                st_f = name + '   ' + url + '\n'
                f.write(st_f.encode('utf8'))

if __name__ == '__main__':
    country_finders = CountryFinder('countries.json')
    country_finders.put_wiki_urls('a.txt')