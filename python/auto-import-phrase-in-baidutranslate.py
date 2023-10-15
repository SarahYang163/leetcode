# coding: utf - 8
import time

import requests

if __name__ == '__main__':

    url = "https://fanyi.baidu.com/pcnewcollection?req=add"

    files = [

    ]
    headers = {
        'Cookie': 'BIDUPSID=C5A0AF20744B6EE39161F805D16F6E71; PSTM=1668605302; newlogin=1; MCITY=-268%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; BAIDUID=08C262AC82222ECBE4EF0AEA26903C38:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; SOUND_PREFER_SWITCH=0; BDUSS=xESG1tSkJ5MjJzT284UUpsZGw5dm9ueURvb1o1QnlhYkFJVk1DOVltcGN1dEZrSVFBQUFBJCQAAAAAAAAAAAEAAACo991Wyq-087XEzqK35wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFwtqmRcLapkcW; BDUSS_BFESS=xESG1tSkJ5MjJzT284UUpsZGw5dm9ueURvb1o1QnlhYkFJVk1DOVltcGN1dEZrSVFBQUFBJCQAAAAAAAAAAAEAAACo991Wyq-087XEzqK35wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFwtqmRcLapkcW; BAIDUID_BFESS=08C262AC82222ECBE4EF0AEA26903C38:FG=1; ZFY=wpFlAQXdtngOPYOSUzHRLoF:Aet:BHSzuEuT0Lx:A4zAu4:C; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1688877151,1688898698,1689077883,1689088253; BA_HECTOR=858h01058ka1ak05a580040v1iaqsbf1p; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=2; delPer=0; H_PS_PSSID=36552_38643_38831_39025_39022_38942_38878_38958_38954_39009_38920_38804_38638_26350_39042_39043_38952; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1689139754; ab_sr=1.0.1_NGRiY2ZhYjdhNjE3MmI4MjllOTliNGYzMDYxODc0MDdlODJmZDIwZTA2MTFiMjA5MjdmNDA2N2M2OGMzNThmNGYwMTRhNDIyYTc3YTRkYjM3ZmZjZjYzNjIyYjgyYWU0ZjUxNzVlNjgwMDJhMTE5YTE0OGI1YWFiNTFkZjE1OWMzNjFiNGM0M2Y2OGQ1M2M4NTg5NmExMGU2N2ZhOTA1ZjZmNmM2Y2MyODcyODA1NjY5M2ZhM2NiOTc5OWZmYWRi'
    }
    try:
        f = open("/Users/sarahyang/Desktop/11.4.3.csv", "r")
        data = f.read()
        array = data.split('\n')
        for arr in array:
            print(arr)
            payload = {
                'fanyi_src': arr,
                'direction': 'en2zh',
                'gid': '2916520',
                'fanyi_dst': '保险类型',
                'bdstoken': '0ff8c5a72edfed3244dfa84decc3a625'
            }
            print(payload)
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            print(response.text)
            time.sleep(0.3)
            # print(response.status_code)
            # assert response.status_code != 200
        f.close()
    except IOError as err:
        print(err)

    # print(response.text)
