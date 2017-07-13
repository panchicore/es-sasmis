import os
import requests
import datetime
import sys

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_PATH = os.path.join(BASE_PATH, "data")

def get(_date_from, _date_to):
    params = {
        "date_a": _date_from,
        "date_b": _date_to,
    }
    res = requests.get(os.environ.get("SOURCE_URL") + "sirs/list/export", params=params)
    print res.url
    print res.json()

    dump = ""

    for i in res.json():
        url = os.environ.get("SOURCE_URL") + "sirs/sir/get"

        params = {
            "id": i["id"],
            "elasticsearch": 1
        }
        incident = requests.get(url, params=params)
        print incident.url

        if incident.ok:
            dump += "{}\n".format(incident.content)
        else:
            print "[ERROR] {}".format(params)

        for sit in range(0, int(i.get("subincidents", 0))):
            params["subincident_index"] = sit + 1
            incident = requests.get(url, params=params)
            print incident.url

            if incident.ok:
                dump += "{}\n".format(incident.content)
            else:
                print "[ERROR] {}".format(params)

    f = open(os.path.join(DOWNLOAD_PATH, "data.json"), 'w')
    f.write(dump)
    f.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # _from_date = datetime.datetime.strptime(sys.argv[1], "%Y-%m-%d")
        # _to_date = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d")
        pass

    today = datetime.date.today()
    back_in = today - datetime.timedelta(days=1)
    get(back_in.isoformat(), today.isoformat())



