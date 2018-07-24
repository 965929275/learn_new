import re
string = "this.className='bigaud_f';javascript:BilingualDict.Click(this,'[图片]https://dictionary.blob.core.chinacloudapi.cn/media/audio/tom/8a/e7/8AE76DF495E14441114FD06473DA2336.mp3','akicon.png',false,'dictionaryvoiceid')"

re = re.findall('https:(.*).mp3', string)
print(re)
