# Grunt task worker to initiate specific bespoke tasks.
from __future__ import division

import shared.database
import json
import ast

db = shared.database.Couchbase(host="couchbase://128.199.62.177")

# product_ids_results = db.run_query('select product_id from job', 'job')

product_ids_results = [
  {
    "product_id": "108600",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "15540",
    "score_change_midpoint_to_present": -20
  },
  {
    "product_id": "206500",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "217120",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "221100",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "223490",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "224440",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "227780",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "228380",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "230290",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "232810",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "233860",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "236370",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "242760",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "244770",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "244850",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "244930",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "246300",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "246880",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "247310",
    "score_change_midpoint_to_present": 11
  },
  {
    "product_id": "248630",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "250540",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "251570",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "251890",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "251950",
    "score_change_midpoint_to_present": 32
  },
  {
    "product_id": "252090",
    "score_change_midpoint_to_present": -14
  },
  {
    "product_id": "252390",
    "score_change_midpoint_to_present": 4
  },
  {
    "product_id": "252770",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "252850",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "252870",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "253250",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "257930",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "259450",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "259570",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "261350",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "263040",
    "score_change_midpoint_to_present": -20
  },
  {
    "product_id": "263200",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "263720",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "263920",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "266190",
    "score_change_midpoint_to_present": -25
  },
  {
    "product_id": "266370",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "266470",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "268650",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "268670",
    "score_change_midpoint_to_present": -23
  },
  {
    "product_id": "268930",
    "score_change_midpoint_to_present": -20
  },
  {
    "product_id": "269350",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "269530",
    "score_change_midpoint_to_present": 12
  },
  {
    "product_id": "269590",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "269610",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "269770",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "274620",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "276870",
    "score_change_midpoint_to_present": -15
  },
  {
    "product_id": "277930",
    "score_change_midpoint_to_present": -18
  },
  {
    "product_id": "280010",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "280720",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "282740",
    "score_change_midpoint_to_present": 27
  },
  {
    "product_id": "283100",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "285110",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "285380",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "285580",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "285920",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "291370",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "292330",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "293220",
    "score_change_midpoint_to_present": 11
  },
  {
    "product_id": "293480",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "293760",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "295110",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "297310",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "297470",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "298280",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "298610",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "299420",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "299580",
    "score_change_midpoint_to_present": 18
  },
  {
    "product_id": "299740",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "300760",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "302590",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "302670",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "302810",
    "score_change_midpoint_to_present": 10
  },
  {
    "product_id": "302830",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "305510",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "305660",
    "score_change_midpoint_to_present": -20
  },
  {
    "product_id": "305840",
    "score_change_midpoint_to_present": -32
  },
  {
    "product_id": "305940",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "305960",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "307090",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "307110",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "307880",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "308080",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "308520",
    "score_change_midpoint_to_present": -13
  },
  {
    "product_id": "311260",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "311310",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "311800",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "312150",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "312210",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "313120",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "315070",
    "score_change_midpoint_to_present": 9
  },
  {
    "product_id": "315330",
    "score_change_midpoint_to_present": -35
  },
  {
    "product_id": "315460",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "315540",
    "score_change_midpoint_to_present": -15
  },
  {
    "product_id": "315840",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "317730",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "318100",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "320240",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "321830",
    "score_change_midpoint_to_present": -14
  },
  {
    "product_id": "321980",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "322300",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "322780",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "323670",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "324080",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "324190",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "324470",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "324510",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "325210",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "325420",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "325430",
    "score_change_midpoint_to_present": -21
  },
  {
    "product_id": "326160",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "326460",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "327070",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "327090",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "327640",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "328080",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "328510",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "328710",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "328740",
    "score_change_midpoint_to_present": -19
  },
  {
    "product_id": "329040",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "329190",
    "score_change_midpoint_to_present": -22
  },
  {
    "product_id": "329310",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "329970",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "330460",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "330570",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "330580",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "331360",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "332500",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "332650",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "333340",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "333640",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "333950",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "335210",
    "score_change_midpoint_to_present": -43
  },
  {
    "product_id": "335850",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "336220",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "337320",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "337950",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "338330",
    "score_change_midpoint_to_present": -22
  },
  {
    "product_id": "338640",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "339440",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "339910",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "340150",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "340210",
    "score_change_midpoint_to_present": -15
  },
  {
    "product_id": "340440",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "340810",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "340960",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "341710",
    "score_change_midpoint_to_present": -14
  },
  {
    "product_id": "342310",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "342530",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "342560",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "342870",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "344040",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "344180",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "344820",
    "score_change_midpoint_to_present": -19
  },
  {
    "product_id": "344890",
    "score_change_midpoint_to_present": -28
  },
  {
    "product_id": "345430",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "346010",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "346330",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "346610",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "346800",
    "score_change_midpoint_to_present": 22
  },
  {
    "product_id": "346970",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "347170",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "347560",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "347600",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "347940",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "349190",
    "score_change_midpoint_to_present": -17
  },
  {
    "product_id": "349250",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "349450",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "349510",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "350150",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "350220",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "351100",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "351290",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "351630",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "352360",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "352430",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "355400",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "355840",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "356510",
    "score_change_midpoint_to_present": -44
  },
  {
    "product_id": "357320",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "357330",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "357770",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "358080",
    "score_change_midpoint_to_present": -15
  },
  {
    "product_id": "360620",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "361420",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "362310",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "362490",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "362620",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "363360",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "363490",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "363950",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "366000",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "366060",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "366090",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "366290",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "366860",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "367030",
    "score_change_midpoint_to_present": -14
  },
  {
    "product_id": "367240",
    "score_change_midpoint_to_present": 9
  },
  {
    "product_id": "367270",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "368340",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "368720",
    "score_change_midpoint_to_present": 9
  },
  {
    "product_id": "368860",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "368980",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "369080",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "369270",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "369560",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "370060",
    "score_change_midpoint_to_present": 4
  },
  {
    "product_id": "370770",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "372740",
    "score_change_midpoint_to_present": -27
  },
  {
    "product_id": "372750",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "372800",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "372820",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "372970",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "373470",
    "score_change_midpoint_to_present": -14
  },
  {
    "product_id": "373750",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "374170",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "374670",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "375480",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "375530",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "376150",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "376880",
    "score_change_midpoint_to_present": -21
  },
  {
    "product_id": "377060",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "377140",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "378280",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "378370",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "378850",
    "score_change_midpoint_to_present": -19
  },
  {
    "product_id": "379210",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "379420",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "381180",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "381750",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "382000",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "382310",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "382480",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "383120",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "384090",
    "score_change_midpoint_to_present": -13
  },
  {
    "product_id": "384960",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "385270",
    "score_change_midpoint_to_present": 7
  },
  {
    "product_id": "385380",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "385890",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "386340",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "386600",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "386650",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "387990",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "389040",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "389050",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "389260",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "390540",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "390560",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "391460",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "391520",
    "score_change_midpoint_to_present": -40
  },
  {
    "product_id": "391530",
    "score_change_midpoint_to_present": -18
  },
  {
    "product_id": "392080",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "393380",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "393390",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "393420",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "393790",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "393820",
    "score_change_midpoint_to_present": -21
  },
  {
    "product_id": "393930",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "394490",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "394690",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "395150",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "396900",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "397100",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "397150",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "397160",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "397750",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "402160",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "402710",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "402800",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "403590",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "404550",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "405010",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "405530",
    "score_change_midpoint_to_present": 4
  },
  {
    "product_id": "405670",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "405710",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "406090",
    "score_change_midpoint_to_present": 6
  },
  {
    "product_id": "409340",
    "score_change_midpoint_to_present": -19
  },
  {
    "product_id": "409490",
    "score_change_midpoint_to_present": -20
  },
  {
    "product_id": "409590",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "410830",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "411600",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "412130",
    "score_change_midpoint_to_present": -21
  },
  {
    "product_id": "412250",
    "score_change_midpoint_to_present": 19
  },
  {
    "product_id": "412310",
    "score_change_midpoint_to_present": -13
  },
  {
    "product_id": "412450",
    "score_change_midpoint_to_present": 4
  },
  {
    "product_id": "412470",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "412860",
    "score_change_midpoint_to_present": 20
  },
  {
    "product_id": "413110",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "413510",
    "score_change_midpoint_to_present": 35
  },
  {
    "product_id": "413740",
    "score_change_midpoint_to_present": 7
  },
  {
    "product_id": "414070",
    "score_change_midpoint_to_present": -15
  },
  {
    "product_id": "414080",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "414120",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "415010",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "415080",
    "score_change_midpoint_to_present": -29
  },
  {
    "product_id": "415590",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "415860",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "416020",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "416240",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "416670",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "418030",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "418110",
    "score_change_midpoint_to_present": 10
  },
  {
    "product_id": "418620",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "418910",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "420550",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "420930",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "422420",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "422860",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "422940",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "423890",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "424370",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "426210",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "426590",
    "score_change_midpoint_to_present": -48
  },
  {
    "product_id": "426930",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "427950",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "428180",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "428610",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "429020",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "429050",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "429790",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "430070",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "431240",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "431450",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "431770",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "432170",
    "score_change_midpoint_to_present": 7
  },
  {
    "product_id": "432250",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "432720",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "433170",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "433630",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "433850",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "437610",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "437890",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "438000",
    "score_change_midpoint_to_present": 7
  },
  {
    "product_id": "438100",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "439340",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "439370",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "439950",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "440280",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "440450",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "440900",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "441230",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "442660",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "442710",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "443890",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "444090",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "444460",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "444650",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "444670",
    "score_change_midpoint_to_present": 4
  },
  {
    "product_id": "444690",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "445220",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "446030",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "446120",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "447960",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "448150",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "448570",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "448640",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "448850",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "449130",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "450540",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "450700",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "451600",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "451650",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "453090",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "453690",
    "score_change_midpoint_to_present": 8
  },
  {
    "product_id": "454140",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "454150",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "454350",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "454680",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "455980",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "457010",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "457140",
    "score_change_midpoint_to_present": 4
  },
  {
    "product_id": "457330",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "458330",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "458520",
    "score_change_midpoint_to_present": 7
  },
  {
    "product_id": "458660",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "458830",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "461210",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "461400",
    "score_change_midpoint_to_present": -38
  },
  {
    "product_id": "461410",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "461430",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "462440",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "462480",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "462940",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "463240",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "463400",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "463530",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "463800",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "463920",
    "score_change_midpoint_to_present": -44
  },
  {
    "product_id": "464470",
    "score_change_midpoint_to_present": -21
  },
  {
    "product_id": "465000",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "465020",
    "score_change_midpoint_to_present": 7
  },
  {
    "product_id": "465200",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "465490",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "466220",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "466560",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "466860",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "466980",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "467010",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "467570",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "467760",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "467820",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "467890",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "467900",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "468070",
    "score_change_midpoint_to_present": 17
  },
  {
    "product_id": "468920",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "469600",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "470310",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "470600",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "471710",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "473910",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "476700",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "477140",
    "score_change_midpoint_to_present": -21
  },
  {
    "product_id": "479010",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "479020",
    "score_change_midpoint_to_present": -14
  },
  {
    "product_id": "481870",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "482440",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "485240",
    "score_change_midpoint_to_present": -18
  },
  {
    "product_id": "485440",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "485900",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "487000",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "487250",
    "score_change_midpoint_to_present": 26
  },
  {
    "product_id": "488150",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "488550",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "488590",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "489380",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "489460",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "489520",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "489940",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "490280",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "490990",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "491470",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "492150",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "495740",
    "score_change_midpoint_to_present": -21
  },
  {
    "product_id": "496240",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "496250",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "496290",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "496440",
    "score_change_midpoint_to_present": 6
  },
  {
    "product_id": "496500",
    "score_change_midpoint_to_present": -21
  },
  {
    "product_id": "497270",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "498340",
    "score_change_midpoint_to_present": -14
  },
  {
    "product_id": "499230",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "500470",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "501220",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "503180",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "503240",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "503370",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "503770",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "504010",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "504050",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "504300",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "504460",
    "score_change_midpoint_to_present": 10
  },
  {
    "product_id": "505460",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "508550",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "508710",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "508790",
    "score_change_midpoint_to_present": 10
  },
  {
    "product_id": "509190",
    "score_change_midpoint_to_present": 6
  },
  {
    "product_id": "509980",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "511430",
    "score_change_midpoint_to_present": 7
  },
  {
    "product_id": "512170",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "512220",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "512900",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "513330",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "513460",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "513590",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "513880",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "516590",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "516750",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "517020",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "517670",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "517720",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "518030",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "518110",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "519080",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "519190",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "520010",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "520530",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "520860",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "520960",
    "score_change_midpoint_to_present": -13
  },
  {
    "product_id": "521150",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "521330",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "523080",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "523960",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "524250",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "524380",
    "score_change_midpoint_to_present": -18
  },
  {
    "product_id": "525210",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "525610",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "525640",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "525680",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "526160",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "526290",
    "score_change_midpoint_to_present": -21
  },
  {
    "product_id": "527230",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "527430",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "528460",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "528550",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "529020",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "529240",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "530560",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "531530",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "531640",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "531660",
    "score_change_midpoint_to_present": 8
  },
  {
    "product_id": "532800",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "533120",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "534000",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "534780",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "535630",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "536660",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "537000",
    "score_change_midpoint_to_present": -14
  },
  {
    "product_id": "537340",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "538100",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "538990",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "539050",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "539400",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "541200",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "541300",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "542770",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "544550",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "545050",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "546150",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "546980",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "547680",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "548560",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "550650",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "550840",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "551170",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "551700",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "552110",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "552620",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "552920",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "553660",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "554570",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "555160",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "555400",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "556640",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "557580",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "558100",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "559650",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "562230",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "562430",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "562500",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "563360",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "563490",
    "score_change_midpoint_to_present": -24
  },
  {
    "product_id": "564050",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "565030",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "566240",
    "score_change_midpoint_to_present": -13
  },
  {
    "product_id": "566860",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "567270",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "567320",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "568220",
    "score_change_midpoint_to_present": 4
  },
  {
    "product_id": "568580",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "569720",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "569770",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "570500",
    "score_change_midpoint_to_present": -18
  },
  {
    "product_id": "570980",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "571740",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "572520",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "573490",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "574070",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "574080",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "574760",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "575850",
    "score_change_midpoint_to_present": -13
  },
  {
    "product_id": "576650",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "576950",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "578620",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "579840",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "581220",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "582890",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "584890",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "585710",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "586950",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "587450",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "587920",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "588120",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "588210",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "588630",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "589290",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "591370",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "591680",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "591790",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "591930",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "592260",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "594650",
    "score_change_midpoint_to_present": -14
  },
  {
    "product_id": "595430",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "595770",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "596280",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "596970",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "597770",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "597920",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "598330",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "598690",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "598700",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "598960",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "599040",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "600460",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "601380",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "601540",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "603040",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "604490",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "605230",
    "score_change_midpoint_to_present": 6
  },
  {
    "product_id": "605450",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "606800",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "607200",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "608110",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "608990",
    "score_change_midpoint_to_present": -9
  },
  {
    "product_id": "609170",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "609410",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "611060",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "611160",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "611500",
    "score_change_midpoint_to_present": 8
  },
  {
    "product_id": "611790",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "611800",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "612470",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "612720",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "612930",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "614860",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "615910",
    "score_change_midpoint_to_present": -17
  },
  {
    "product_id": "616330",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "616720",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "617030",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "617480",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "619080",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "619340",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "621880",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "622040",
    "score_change_midpoint_to_present": -12
  },
  {
    "product_id": "622470",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "622870",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "624890",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "626550",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "627070",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "627690",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "628190",
    "score_change_midpoint_to_present": 4
  },
  {
    "product_id": "628710",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "629220",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "630030",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "630900",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "632300",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "635000",
    "score_change_midpoint_to_present": -66
  },
  {
    "product_id": "636480",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "636690",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "636970",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "638000",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "638850",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "639230",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "640210",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "640310",
    "score_change_midpoint_to_present": 6
  },
  {
    "product_id": "640800",
    "score_change_midpoint_to_present": -10
  },
  {
    "product_id": "641960",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "642770",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "643810",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "644670",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "644930",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "646570",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "647410",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "647530",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "649900",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "650350",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "650940",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "651280",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "654690",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "655780",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "656200",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "656530",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "657240",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "657990",
    "score_change_midpoint_to_present": -14
  },
  {
    "product_id": "658980",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "659540",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "659920",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "661920",
    "score_change_midpoint_to_present": -21
  },
  {
    "product_id": "663300",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "664000",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "664750",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "665040",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "666020",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "666140",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "667810",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "667970",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "669320",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "670160",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "670490",
    "score_change_midpoint_to_present": -13
  },
  {
    "product_id": "671440",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "671510",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "672630",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "673610",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "673750",
    "score_change_midpoint_to_present": 9
  },
  {
    "product_id": "676760",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "679260",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "679270",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "679400",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "680440",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "680860",
    "score_change_midpoint_to_present": -18
  },
  {
    "product_id": "681060",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "681280",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "681330",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "681390",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "682140",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "682530",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "683770",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "685420",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "685690",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "686200",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "686260",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "686680",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "687630",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "688360",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "689620",
    "score_change_midpoint_to_present": -13
  },
  {
    "product_id": "689700",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "690040",
    "score_change_midpoint_to_present": 4
  },
  {
    "product_id": "690510",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "690610",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "691320",
    "score_change_midpoint_to_present": -11
  },
  {
    "product_id": "691390",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "693580",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "693750",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "696370",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "696650",
    "score_change_midpoint_to_present": 3
  },
  {
    "product_id": "698260",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "698640",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "699390",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "700570",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "700770",
    "score_change_midpoint_to_present": -7
  },
  {
    "product_id": "704030",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "704470",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "704510",
    "score_change_midpoint_to_present": 4
  },
  {
    "product_id": "704830",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "705100",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "706020",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "707590",
    "score_change_midpoint_to_present": -13
  },
  {
    "product_id": "710610",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "711440",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "713460",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "714010",
    "score_change_midpoint_to_present": -16
  },
  {
    "product_id": "716380",
    "score_change_midpoint_to_present": -4
  },
  {
    "product_id": "717790",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "718650",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "719590",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "722670",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "722730",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "724470",
    "score_change_midpoint_to_present": -3
  },
  {
    "product_id": "725960",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "726250",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "728730",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "734580",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "735850",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "738500",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "738610",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "740290",
    "score_change_midpoint_to_present": 1
  },
  {
    "product_id": "741430",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "742460",
    "score_change_midpoint_to_present": -6
  },
  {
    "product_id": "746930",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "747100",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "748370",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "749540",
    "score_change_midpoint_to_present": -8
  },
  {
    "product_id": "752910",
    "score_change_midpoint_to_present": 5
  },
  {
    "product_id": "755770",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "756360",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "757240",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "758190",
    "score_change_midpoint_to_present": -1
  },
  {
    "product_id": "763430",
    "score_change_midpoint_to_present": -2
  },
  {
    "product_id": "765250",
    "score_change_midpoint_to_present": -5
  },
  {
    "product_id": "775940",
    "score_change_midpoint_to_present": 2
  },
  {
    "product_id": "786410",
    "score_change_midpoint_to_present": -9
  }
]

overall_results = []

for row1 in product_ids_results:

    product_id = row1['product_id']

    print "Working on " + product_id

    error = True

    ccu_range_start = -1
    ccu_range_end = -1

    while error:
        # try:
            results = db.run_query(
                'select `values`, `start` from `usage` where product_id="' + str(product_id) + '"', 'job')

            values = []
            start = -1
            for row in results:
                values = ast.literal_eval(row['values'])
                start = int(row['start'])

                ccu_range_start = start
                ccu_range_end = start + 86400 * len(values)

            error = False
        # except Exception, e:
        #     print "Timed out on {0}, trying again.".format(product_id)

    latest_start = ccu_range_start
    earliest_end = ccu_range_end

    print("From " + str(latest_start) + " to " + str(earliest_end))

    results = db.run_query(
        'select count(*) as cnt from `update` where product_id="' + str(product_id) + '" and date_created >= ' + str(latest_start) + " and date_created <=" + str(earliest_end), 'job')

    update_count = -1
    for row in results:
        update_count = row['cnt']

    four_weeks = 2419200
    p_range = earliest_end - latest_start

    frequency = (update_count / p_range) * four_weeks

    row1['update_frequency_per_four_weeks'] = round(frequency, 2)

    overall_results.append(row1)

print "Finally"
# overall_results.sort(key=lambda x: x['day_start_time'])
print overall_results
# print len(overall_results)