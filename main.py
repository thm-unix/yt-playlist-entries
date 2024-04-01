import sys
import requests
import json


class Video:
    title = ''
    uploader = ''

    def __init__(self, title, uploader):
        self.title = title
        self.uploader = uploader


def downloadWebPage(url):
    r = requests.get(url)
    html = r.text
    return html


def getJSONObject(html):
    # Closer to the end of the HTML page there is definition of
    # 'ytInitialData' object that contains all data about the
    # playlist in JSON format. Getting & returning it...

    searchKey = 'var ytInitialData = '
    html2 = html[html.find(searchKey) + len(searchKey):]
    html3 = html2[:html2.find('</script>') - 1]
    return json.loads(html3)


def getVideoInfo(playlist):
    videoInfo = []

    contents = playlist['contents']
    videoList = contents[('twoColumnBrowse'
            'ResultsRenderer')]['tabs'][0][('tab'
            'Renderer')]['content'][('sectionList'
            'Renderer')]['contents'][0][('itemSection'
            'Renderer')]['contents'][0]['playlistVideoListRenderer']\
            ['contents']

    for videoObject in videoList:
        title = videoObject['playlistVideoRenderer']['title']\
                           ['runs'][0]['text']

        uploader = videoObject['playlistVideoRenderer']['shortBylineText']\
                              ['runs'][0]['text']

        video = Video(title, uploader)
        videoInfo.append(video)

    return videoInfo


def writeResult(lst):
    with open('result.txt', 'w') as file:
        for video in lst:
            file.write(f'{video.title}  |  {video.uploader}\n')


def usage(argv):
    print(f'Usage: {argv[0]} PLAYLIST_LINK')

def main(argv):
    print('yt-playlist-entries')
    print('v. 0.0.1')
    print('by thm-unix')
    print('https://thm-unix.github.io/')
    print('2024')

    print()

    if len(argv) == 2:
        print('[i] Downloading HTML page...')
        html = downloadWebPage(argv[1])
        print('[i] Getting playlist JSON object...')
        playlistObj = getJSONObject(html)
        print('[i] Getting list of videos from the JSON object...')
        videoInfo = getVideoInfo(playlistObj)
        print('[i] Writing to result.txt...')
        writeResult(videoInfo)

        cwd = __file__[:__file__.rfind('/')]
        print(f'[+] SUCCESS! List available at {cwd}/result.txt')
    else:
        usage(argv)


if __name__ == '__main__':
    main(sys.argv)
