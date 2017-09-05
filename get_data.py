import os
import requests
import datetime
import sys


def hydrate(incident):
    incident["@timestamp"] = incident["incident_date_complete"]
    incident["location"] = {"lat": incident["latitude"], "lon": incident["longitude"]}
    return incident

def index(incident):
    index_url = os.environ['ES_SASMIS_HOST'] + os.environ['ES_SASMIS_INDEX'] + "/incident/" + str(incident["id"])
    print index_url
    res = requests.post(index_url, json=hydrate(incident))
    if not res.ok:
        print incident
        print res, res.content
        print '------'

def get(_date_from, _date_to, updated_since=None):
    params = {
        "date_a": _date_from or "",
        "date_b": _date_to or "",
        "updated_since": "0"
    }

    if updated_since:
        params["updated_since"] = updated_since

    res = requests.get(os.environ.get("SASMIS_SOURCE_URL") + "sirs/list/export", params=params)
    print res.url
    print res
    # print res.content

    print "> {0} incidents".format(len(res.json()))

    for i in res.json():
        url = os.environ.get("SASMIS_SOURCE_URL") + "sirs/sir/get"

        params = {
            "id": i["id"],
            "elasticsearch": 1
        }
        incident = requests.get(url, params=params)
        print incident.url

        if incident.ok:
            index(incident.json())
        else:
            print "[ERROR] {}".format(params)

        for sit in range(0, int(i.get("subincidents", 0))):
            params["subincident_index"] = sit + 1
            incident = requests.get(url, params=params)
            print incident.url

            if incident.ok:
                index(incident.json())
            else:
                print "[ERROR] {}".format(params)


if __name__ == "__main__":

    if len(sys.argv) == 2:

        today = datetime.date.today()
        back_in = today - datetime.timedelta(days=1)
        get(None, None, back_in)
    elif len(sys.argv) == 3:
        _from_date = datetime.datetime.strptime(sys.argv[1], "%Y-%m-%d").date().isoformat()
        _to_date = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d").date().isoformat()
        get(_from_date, _to_date)



