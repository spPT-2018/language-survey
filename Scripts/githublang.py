try:
  import json
except ImportError:
  import simplejson as json
import urllib

user = unicode(raw_input('Enter username: '))
repos = json.loads(urllib.urlopen(u'https://api.github.com/users/%s/repos?per_page=100' % user).read())
def reducer(stats, lang):
  if lang:
    stats[lang] = stats.setdefault(lang, 0) + 1
  return whole

lang_stats = reduce(reducer, (repo["language"] for repo in repos), {})
lang_list_sorted = sorted(lang_stats, key=lambda l:lang_stats[l], reverse=True)
print(lang_list_sorted)
