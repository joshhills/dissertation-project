# Grunt task worker to initiate specific bespoke tasks.

from couchbase.n1ql import N1QLQuery

import shared.database

db = shared.database.Couchbase(host="couchbase://128.199.62.177")

overall = []

for i in range(101):
    print i

    query = ("""select t.cnt from
    [
      {
        "cnt": 20,
        "product_id": "598720"
      },
      {
        "cnt": 20,
        "product_id": "447100"
      },
      {
        "cnt": 20,
        "product_id": "683690"
      },
      {
        "cnt": 20,
        "product_id": "708890"
      },
      {
        "cnt": 20,
        "product_id": "693790"
      },
      {
        "cnt": 20,
        "product_id": "489400"
      },
      {
        "cnt": 20,
        "product_id": "242610"
      },
      {
        "cnt": 20,
        "product_id": "672790"
      },
      {
        "cnt": 20,
        "product_id": "425450"
      },
      {
        "cnt": 21,
        "product_id": "526130"
      },
      {
        "cnt": 21,
        "product_id": "572220"
      },
      {
        "cnt": 21,
        "product_id": "572230"
      },
      {
        "cnt": 21,
        "product_id": "373120"
      },
      {
        "cnt": 21,
        "product_id": "369700"
      },
      {
        "cnt": 21,
        "product_id": "575430"
      },
      {
        "cnt": 21,
        "product_id": "450020"
      },
      {
        "cnt": 22,
        "product_id": "305460"
      },
      {
        "cnt": 22,
        "product_id": "463400"
      },
      {
        "cnt": 22,
        "product_id": "684040"
      },
      {
        "cnt": 22,
        "product_id": "666730"
      },
      {
        "cnt": 22,
        "product_id": "522130"
      },
      {
        "cnt": 22,
        "product_id": "623540"
      },
      {
        "cnt": 22,
        "product_id": "626250"
      },
      {
        "cnt": 22,
        "product_id": "623380"
      },
      {
        "cnt": 22,
        "product_id": "666820"
      },
      {
        "cnt": 22,
        "product_id": "517170"
      },
      {
        "cnt": 22,
        "product_id": "432480"
      },
      {
        "cnt": 22,
        "product_id": "327960"
      },
      {
        "cnt": 22,
        "product_id": "606920"
      },
      {
        "cnt": 22,
        "product_id": "512420"
      },
      {
        "cnt": 22,
        "product_id": "355490"
      },
      {
        "cnt": 23,
        "product_id": "598170"
      },
      {
        "cnt": 23,
        "product_id": "467400"
      },
      {
        "cnt": 23,
        "product_id": "513760"
      },
      {
        "cnt": 23,
        "product_id": "644420"
      },
      {
        "cnt": 23,
        "product_id": "448230"
      },
      {
        "cnt": 23,
        "product_id": "525350"
      },
      {
        "cnt": 23,
        "product_id": "566430"
      },
      {
        "cnt": 23,
        "product_id": "575850"
      },
      {
        "cnt": 23,
        "product_id": "615020"
      },
      {
        "cnt": 24,
        "product_id": "624830"
      },
      {
        "cnt": 24,
        "product_id": "362940"
      },
      {
        "cnt": 24,
        "product_id": "596280"
      },
      {
        "cnt": 24,
        "product_id": "765180"
      },
      {
        "cnt": 24,
        "product_id": "282740"
      },
      {
        "cnt": 24,
        "product_id": "341270"
      },
      {
        "cnt": 24,
        "product_id": "412860"
      },
      {
        "cnt": 25,
        "product_id": "496440"
      },
      {
        "cnt": 25,
        "product_id": "404070"
      },
      {
        "cnt": 25,
        "product_id": "576950"
      },
      {
        "cnt": 25,
        "product_id": "335210"
      },
      {
        "cnt": 25,
        "product_id": "425230"
      },
      {
        "cnt": 25,
        "product_id": "388910"
      },
      {
        "cnt": 25,
        "product_id": "704470"
      },
      {
        "cnt": 25,
        "product_id": "575970"
      },
      {
        "cnt": 25,
        "product_id": "492410"
      },
      {
        "cnt": 25,
        "product_id": "395150"
      },
      {
        "cnt": 25,
        "product_id": "503390"
      },
      {
        "cnt": 25,
        "product_id": "518110"
      },
      {
        "cnt": 25,
        "product_id": "470280"
      },
      {
        "cnt": 25,
        "product_id": "527790"
      },
      {
        "cnt": 26,
        "product_id": "588630"
      },
      {
        "cnt": 26,
        "product_id": "715410"
      },
      {
        "cnt": 26,
        "product_id": "498630"
      },
      {
        "cnt": 26,
        "product_id": "429430"
      },
      {
        "cnt": 26,
        "product_id": "448060"
      },
      {
        "cnt": 26,
        "product_id": "706840"
      },
      {
        "cnt": 26,
        "product_id": "555970"
      },
      {
        "cnt": 26,
        "product_id": "393170"
      },
      {
        "cnt": 27,
        "product_id": "474890"
      },
      {
        "cnt": 27,
        "product_id": "640300"
      },
      {
        "cnt": 27,
        "product_id": "336220"
      },
      {
        "cnt": 27,
        "product_id": "670260"
      },
      {
        "cnt": 27,
        "product_id": "713460"
      },
      {
        "cnt": 27,
        "product_id": "666310"
      },
      {
        "cnt": 27,
        "product_id": "422210"
      },
      {
        "cnt": 27,
        "product_id": "765250"
      },
      {
        "cnt": 27,
        "product_id": "335940"
      },
      {
        "cnt": 27,
        "product_id": "493400"
      },
      {
        "cnt": 28,
        "product_id": "449130"
      },
      {
        "cnt": 28,
        "product_id": "701380"
      },
      {
        "cnt": 28,
        "product_id": "463870"
      },
      {
        "cnt": 28,
        "product_id": "663350"
      },
      {
        "cnt": 28,
        "product_id": "496290"
      },
      {
        "cnt": 28,
        "product_id": "599040"
      },
      {
        "cnt": 28,
        "product_id": "589250"
      },
      {
        "cnt": 28,
        "product_id": "597920"
      },
      {
        "cnt": 28,
        "product_id": "525210"
      },
      {
        "cnt": 29,
        "product_id": "339820"
      },
      {
        "cnt": 29,
        "product_id": "509260"
      },
      {
        "cnt": 29,
        "product_id": "756600"
      },
      {
        "cnt": 29,
        "product_id": "611770"
      },
      {
        "cnt": 29,
        "product_id": "639220"
      },
      {
        "cnt": 29,
        "product_id": "598180"
      },
      {
        "cnt": 29,
        "product_id": "500470"
      },
      {
        "cnt": 29,
        "product_id": "523080"
      },
      {
        "cnt": 29,
        "product_id": "412250"
      },
      {
        "cnt": 29,
        "product_id": "683770"
      },
      {
        "cnt": 29,
        "product_id": "508710"
      },
      {
        "cnt": 30,
        "product_id": "369270"
      },
      {
        "cnt": 30,
        "product_id": "681060"
      },
      {
        "cnt": 30,
        "product_id": "529020"
      },
      {
        "cnt": 30,
        "product_id": "441230"
      },
      {
        "cnt": 30,
        "product_id": "374170"
      },
      {
        "cnt": 30,
        "product_id": "616330"
      },
      {
        "cnt": 30,
        "product_id": "657280"
      },
      {
        "cnt": 30,
        "product_id": "513250"
      },
      {
        "cnt": 30,
        "product_id": "727460"
      },
      {
        "cnt": 30,
        "product_id": "716380"
      },
      {
        "cnt": 30,
        "product_id": "688880"
      },
      {
        "cnt": 30,
        "product_id": "434530"
      },
      {
        "cnt": 30,
        "product_id": "585190"
      },
      {
        "cnt": 30,
        "product_id": "537000"
      },
      {
        "cnt": 31,
        "product_id": "724470"
      },
      {
        "cnt": 31,
        "product_id": "545600"
      },
      {
        "cnt": 31,
        "product_id": "580820"
      },
      {
        "cnt": 31,
        "product_id": "689520"
      },
      {
        "cnt": 31,
        "product_id": "568400"
      },
      {
        "cnt": 31,
        "product_id": "398120"
      },
      {
        "cnt": 31,
        "product_id": "482440"
      },
      {
        "cnt": 31,
        "product_id": "682530"
      },
      {
        "cnt": 31,
        "product_id": "602480"
      },
      {
        "cnt": 31,
        "product_id": "548650"
      },
      {
        "cnt": 31,
        "product_id": "458410"
      },
      {
        "cnt": 31,
        "product_id": "338330"
      },
      {
        "cnt": 31,
        "product_id": "488150"
      },
      {
        "cnt": 31,
        "product_id": "523960"
      },
      {
        "cnt": 32,
        "product_id": "563490"
      },
      {
        "cnt": 32,
        "product_id": "405530"
      },
      {
        "cnt": 32,
        "product_id": "587920"
      },
      {
        "cnt": 32,
        "product_id": "378530"
      },
      {
        "cnt": 33,
        "product_id": "535630"
      },
      {
        "cnt": 33,
        "product_id": "696650"
      },
      {
        "cnt": 33,
        "product_id": "465450"
      },
      {
        "cnt": 33,
        "product_id": "718010"
      },
      {
        "cnt": 33,
        "product_id": "500480"
      },
      {
        "cnt": 33,
        "product_id": "611060"
      },
      {
        "cnt": 33,
        "product_id": "693580"
      },
      {
        "cnt": 33,
        "product_id": "458030"
      },
      {
        "cnt": 33,
        "product_id": "546210"
      },
      {
        "cnt": 33,
        "product_id": "366860"
      },
      {
        "cnt": 34,
        "product_id": "302810"
      },
      {
        "cnt": 34,
        "product_id": "504010"
      },
      {
        "cnt": 34,
        "product_id": "458330"
      },
      {
        "cnt": 34,
        "product_id": "689570"
      },
      {
        "cnt": 34,
        "product_id": "747100"
      },
      {
        "cnt": 34,
        "product_id": "407700"
      },
      {
        "cnt": 34,
        "product_id": "438000"
      },
      {
        "cnt": 34,
        "product_id": "463240"
      },
      {
        "cnt": 34,
        "product_id": "541200"
      },
      {
        "cnt": 34,
        "product_id": "349190"
      },
      {
        "cnt": 34,
        "product_id": "619340"
      },
      {
        "cnt": 34,
        "product_id": "577970"
      },
      {
        "cnt": 34,
        "product_id": "413740"
      },
      {
        "cnt": 34,
        "product_id": "714640"
      },
      {
        "cnt": 35,
        "product_id": "467060"
      },
      {
        "cnt": 35,
        "product_id": "609170"
      },
      {
        "cnt": 35,
        "product_id": "340440"
      },
      {
        "cnt": 35,
        "product_id": "362310"
      },
      {
        "cnt": 35,
        "product_id": "673750"
      },
      {
        "cnt": 35,
        "product_id": "763430"
      },
      {
        "cnt": 35,
        "product_id": "543650"
      },
      {
        "cnt": 35,
        "product_id": "522730"
      },
      {
        "cnt": 35,
        "product_id": "375550"
      },
      {
        "cnt": 35,
        "product_id": "462940"
      },
      {
        "cnt": 35,
        "product_id": "413510"
      },
      {
        "cnt": 36,
        "product_id": "650940"
      },
      {
        "cnt": 36,
        "product_id": "556070"
      },
      {
        "cnt": 36,
        "product_id": "437550"
      },
      {
        "cnt": 36,
        "product_id": "426210"
      },
      {
        "cnt": 36,
        "product_id": "347660"
      },
      {
        "cnt": 36,
        "product_id": "704510"
      },
      {
        "cnt": 36,
        "product_id": "458660"
      },
      {
        "cnt": 36,
        "product_id": "665040"
      },
      {
        "cnt": 37,
        "product_id": "467890"
      },
      {
        "cnt": 37,
        "product_id": "364670"
      },
      {
        "cnt": 37,
        "product_id": "488590"
      },
      {
        "cnt": 37,
        "product_id": "588560"
      },
      {
        "cnt": 37,
        "product_id": "501740"
      },
      {
        "cnt": 37,
        "product_id": "436480"
      },
      {
        "cnt": 38,
        "product_id": "328740"
      },
      {
        "cnt": 38,
        "product_id": "786410"
      },
      {
        "cnt": 38,
        "product_id": "591680"
      },
      {
        "cnt": 38,
        "product_id": "381800"
      },
      {
        "cnt": 39,
        "product_id": "464690"
      },
      {
        "cnt": 39,
        "product_id": "535160"
      },
      {
        "cnt": 39,
        "product_id": "605230"
      },
      {
        "cnt": 39,
        "product_id": "627070"
      },
      {
        "cnt": 39,
        "product_id": "378280"
      },
      {
        "cnt": 39,
        "product_id": "366060"
      },
      {
        "cnt": 40,
        "product_id": "372970"
      },
      {
        "cnt": 40,
        "product_id": "699390"
      },
      {
        "cnt": 40,
        "product_id": "639230"
      },
      {
        "cnt": 40,
        "product_id": "433630"
      },
      {
        "cnt": 40,
        "product_id": "585710"
      },
      {
        "cnt": 40,
        "product_id": "538990"
      },
      {
        "cnt": 40,
        "product_id": "635000"
      },
      {
        "cnt": 41,
        "product_id": "725960"
      },
      {
        "cnt": 41,
        "product_id": "741430"
      },
      {
        "cnt": 41,
        "product_id": "397730"
      },
      {
        "cnt": 41,
        "product_id": "592490"
      },
      {
        "cnt": 41,
        "product_id": "485240"
      },
      {
        "cnt": 41,
        "product_id": "465020"
      },
      {
        "cnt": 41,
        "product_id": "700770"
      },
      {
        "cnt": 41,
        "product_id": "402800"
      },
      {
        "cnt": 41,
        "product_id": "448150"
      },
      {
        "cnt": 41,
        "product_id": "707590"
      },
      {
        "cnt": 42,
        "product_id": "758990"
      },
      {
        "cnt": 42,
        "product_id": "394490"
      },
      {
        "cnt": 42,
        "product_id": "659920"
      },
      {
        "cnt": 42,
        "product_id": "376150"
      },
      {
        "cnt": 42,
        "product_id": "372740"
      },
      {
        "cnt": 42,
        "product_id": "742460"
      },
      {
        "cnt": 42,
        "product_id": "690610"
      },
      {
        "cnt": 42,
        "product_id": "576650"
      },
      {
        "cnt": 42,
        "product_id": "676760"
      },
      {
        "cnt": 42,
        "product_id": "463800"
      },
      {
        "cnt": 42,
        "product_id": "443890"
      },
      {
        "cnt": 43,
        "product_id": "693750"
      },
      {
        "cnt": 43,
        "product_id": "551860"
      },
      {
        "cnt": 43,
        "product_id": "497270"
      },
      {
        "cnt": 43,
        "product_id": "524250"
      },
      {
        "cnt": 43,
        "product_id": "340960"
      },
      {
        "cnt": 43,
        "product_id": "479020"
      },
      {
        "cnt": 43,
        "product_id": "664000"
      },
      {
        "cnt": 44,
        "product_id": "391530"
      },
      {
        "cnt": 44,
        "product_id": "513460"
      },
      {
        "cnt": 44,
        "product_id": "462480"
      },
      {
        "cnt": 44,
        "product_id": "624890"
      },
      {
        "cnt": 44,
        "product_id": "416000"
      },
      {
        "cnt": 44,
        "product_id": "640800"
      },
      {
        "cnt": 44,
        "product_id": "518040"
      },
      {
        "cnt": 45,
        "product_id": "494310"
      },
      {
        "cnt": 45,
        "product_id": "314300"
      },
      {
        "cnt": 45,
        "product_id": "329310"
      },
      {
        "cnt": 45,
        "product_id": "440450"
      },
      {
        "cnt": 45,
        "product_id": "680860"
      },
      {
        "cnt": 45,
        "product_id": "405670"
      },
      {
        "cnt": 45,
        "product_id": "664750"
      },
      {
        "cnt": 45,
        "product_id": "447960"
      },
      {
        "cnt": 46,
        "product_id": "520960"
      },
      {
        "cnt": 46,
        "product_id": "603040"
      },
      {
        "cnt": 46,
        "product_id": "691320"
      },
      {
        "cnt": 46,
        "product_id": "344890"
      },
      {
        "cnt": 47,
        "product_id": "526290"
      },
      {
        "cnt": 47,
        "product_id": "659540"
      },
      {
        "cnt": 47,
        "product_id": "340210"
      },
      {
        "cnt": 47,
        "product_id": "572010"
      },
      {
        "cnt": 47,
        "product_id": "609410"
      },
      {
        "cnt": 47,
        "product_id": "501220"
      },
      {
        "cnt": 48,
        "product_id": "521330"
      },
      {
        "cnt": 48,
        "product_id": "397750"
      },
      {
        "cnt": 48,
        "product_id": "539050"
      },
      {
        "cnt": 48,
        "product_id": "305660"
      },
      {
        "cnt": 48,
        "product_id": "357320"
      },
      {
        "cnt": 48,
        "product_id": "630900"
      },
      {
        "cnt": 48,
        "product_id": "344180"
      },
      {
        "cnt": 49,
        "product_id": "680440"
      },
      {
        "cnt": 49,
        "product_id": "554570"
      },
      {
        "cnt": 49,
        "product_id": "477140"
      },
      {
        "cnt": 49,
        "product_id": "440280"
      },
      {
        "cnt": 50,
        "product_id": "299580"
      },
      {
        "cnt": 50,
        "product_id": "367240"
      },
      {
        "cnt": 50,
        "product_id": "393820"
      },
      {
        "cnt": 50,
        "product_id": "485440"
      },
      {
        "cnt": 51,
        "product_id": "470310"
      },
      {
        "cnt": 51,
        "product_id": "428610"
      },
      {
        "cnt": 51,
        "product_id": "642770"
      },
      {
        "cnt": 51,
        "product_id": "411600"
      },
      {
        "cnt": 52,
        "product_id": "367030"
      },
      {
        "cnt": 52,
        "product_id": "570500"
      },
      {
        "cnt": 52,
        "product_id": "432170"
      },
      {
        "cnt": 52,
        "product_id": "373470"
      },
      {
        "cnt": 53,
        "product_id": "626550"
      },
      {
        "cnt": 53,
        "product_id": "591930"
      },
      {
        "cnt": 53,
        "product_id": "640210"
      },
      {
        "cnt": 53,
        "product_id": "511430"
      },
      {
        "cnt": 53,
        "product_id": "503180"
      },
      {
        "cnt": 53,
        "product_id": "410830"
      },
      {
        "cnt": 54,
        "product_id": "710610"
      },
      {
        "cnt": 54,
        "product_id": "681330"
      },
      {
        "cnt": 54,
        "product_id": "513880"
      },
      {
        "cnt": 54,
        "product_id": "376880"
      },
      {
        "cnt": 54,
        "product_id": "711440"
      },
      {
        "cnt": 54,
        "product_id": "266470"
      },
      {
        "cnt": 54,
        "product_id": "569720"
      },
      {
        "cnt": 55,
        "product_id": "752910"
      },
      {
        "cnt": 55,
        "product_id": "688360"
      },
      {
        "cnt": 55,
        "product_id": "217120"
      },
      {
        "cnt": 55,
        "product_id": "461410"
      },
      {
        "cnt": 56,
        "product_id": "539400"
      },
      {
        "cnt": 56,
        "product_id": "465000"
      },
      {
        "cnt": 56,
        "product_id": "718090"
      },
      {
        "cnt": 56,
        "product_id": "349510"
      },
      {
        "cnt": 57,
        "product_id": "552880"
      },
      {
        "cnt": 57,
        "product_id": "500420"
      },
      {
        "cnt": 57,
        "product_id": "615910"
      },
      {
        "cnt": 58,
        "product_id": "546150"
      },
      {
        "cnt": 58,
        "product_id": "349450"
      },
      {
        "cnt": 58,
        "product_id": "430070"
      },
      {
        "cnt": 59,
        "product_id": "749540"
      },
      {
        "cnt": 59,
        "product_id": "579840"
      },
      {
        "cnt": 59,
        "product_id": "355420"
      },
      {
        "cnt": 59,
        "product_id": "726250"
      },
      {
        "cnt": 60,
        "product_id": "689620"
      },
      {
        "cnt": 60,
        "product_id": "628190"
      },
      {
        "cnt": 60,
        "product_id": "342870"
      },
      {
        "cnt": 60,
        "product_id": "651280"
      },
      {
        "cnt": 60,
        "product_id": "352360"
      },
      {
        "cnt": 60,
        "product_id": "442660"
      },
      {
        "cnt": 60,
        "product_id": "548560"
      },
      {
        "cnt": 60,
        "product_id": "261350"
      },
      {
        "cnt": 61,
        "product_id": "490280"
      },
      {
        "cnt": 61,
        "product_id": "517020"
      },
      {
        "cnt": 61,
        "product_id": "597770"
      },
      {
        "cnt": 61,
        "product_id": "409490"
      },
      {
        "cnt": 62,
        "product_id": "595770"
      },
      {
        "cnt": 62,
        "product_id": "444650"
      },
      {
        "cnt": 62,
        "product_id": "628710"
      },
      {
        "cnt": 62,
        "product_id": "426590"
      },
      {
        "cnt": 63,
        "product_id": "509190"
      },
      {
        "cnt": 63,
        "product_id": "252090"
      },
      {
        "cnt": 63,
        "product_id": "439950"
      },
      {
        "cnt": 63,
        "product_id": "532800"
      },
      {
        "cnt": 64,
        "product_id": "588120"
      },
      {
        "cnt": 64,
        "product_id": "667810"
      },
      {
        "cnt": 64,
        "product_id": "705100"
      },
      {
        "cnt": 64,
        "product_id": "389260"
      },
      {
        "cnt": 65,
        "product_id": "647410"
      },
      {
        "cnt": 65,
        "product_id": "682140"
      },
      {
        "cnt": 65,
        "product_id": "557580"
      },
      {
        "cnt": 65,
        "product_id": "372380"
      },
      {
        "cnt": 65,
        "product_id": "622870"
      },
      {
        "cnt": 65,
        "product_id": "416260"
      },
      {
        "cnt": 66,
        "product_id": "687630"
      },
      {
        "cnt": 66,
        "product_id": "416240"
      },
      {
        "cnt": 66,
        "product_id": "670490"
      },
      {
        "cnt": 67,
        "product_id": "431770"
      },
      {
        "cnt": 67,
        "product_id": "576940"
      },
      {
        "cnt": 67,
        "product_id": "563360"
      },
      {
        "cnt": 67,
        "product_id": "432720"
      },
      {
        "cnt": 67,
        "product_id": "536660"
      },
      {
        "cnt": 68,
        "product_id": "567270"
      },
      {
        "cnt": 68,
        "product_id": "498340"
      },
      {
        "cnt": 69,
        "product_id": "722670"
      },
      {
        "cnt": 69,
        "product_id": "512170"
      },
      {
        "cnt": 69,
        "product_id": "453690"
      },
      {
        "cnt": 69,
        "product_id": "700570"
      },
      {
        "cnt": 69,
        "product_id": "346800"
      },
      {
        "cnt": 70,
        "product_id": "429020"
      },
      {
        "cnt": 70,
        "product_id": "342530"
      },
      {
        "cnt": 70,
        "product_id": "503240"
      },
      {
        "cnt": 71,
        "product_id": "378850"
      },
      {
        "cnt": 71,
        "product_id": "311980"
      },
      {
        "cnt": 71,
        "product_id": "444670"
      },
      {
        "cnt": 71,
        "product_id": "346610"
      },
      {
        "cnt": 72,
        "product_id": "454580"
      },
      {
        "cnt": 72,
        "product_id": "738610"
      },
      {
        "cnt": 72,
        "product_id": "349250"
      },
      {
        "cnt": 73,
        "product_id": "308520"
      },
      {
        "cnt": 73,
        "product_id": "493280"
      },
      {
        "cnt": 73,
        "product_id": "390540"
      },
      {
        "cnt": 73,
        "product_id": "495740"
      },
      {
        "cnt": 74,
        "product_id": "446030"
      },
      {
        "cnt": 74,
        "product_id": "567320"
      },
      {
        "cnt": 74,
        "product_id": "598060"
      },
      {
        "cnt": 75,
        "product_id": "252390"
      },
      {
        "cnt": 75,
        "product_id": "512560"
      },
      {
        "cnt": 75,
        "product_id": "775940"
      },
      {
        "cnt": 75,
        "product_id": "562430"
      },
      {
        "cnt": 75,
        "product_id": "467900"
      },
      {
        "cnt": 76,
        "product_id": "268930"
      },
      {
        "cnt": 76,
        "product_id": "415080"
      },
      {
        "cnt": 76,
        "product_id": "657990"
      },
      {
        "cnt": 77,
        "product_id": "467010"
      },
      {
        "cnt": 77,
        "product_id": "467760"
      },
      {
        "cnt": 77,
        "product_id": "504460"
      },
      {
        "cnt": 77,
        "product_id": "477180"
      },
      {
        "cnt": 78,
        "product_id": "355400"
      },
      {
        "cnt": 78,
        "product_id": "714010"
      },
      {
        "cnt": 78,
        "product_id": "581220"
      },
      {
        "cnt": 79,
        "product_id": "386340"
      },
      {
        "cnt": 79,
        "product_id": "647530"
      },
      {
        "cnt": 79,
        "product_id": "325430"
      },
      {
        "cnt": 79,
        "product_id": "338640"
      },
      {
        "cnt": 80,
        "product_id": "269530"
      },
      {
        "cnt": 80,
        "product_id": "503010"
      },
      {
        "cnt": 80,
        "product_id": "630030"
      },
      {
        "cnt": 80,
        "product_id": "601380"
      },
      {
        "cnt": 80,
        "product_id": "499230"
      },
      {
        "cnt": 81,
        "product_id": "479010"
      },
      {
        "cnt": 81,
        "product_id": "644670"
      },
      {
        "cnt": 81,
        "product_id": "640310"
      },
      {
        "cnt": 81,
        "product_id": "596970"
      },
      {
        "cnt": 82,
        "product_id": "250540"
      },
      {
        "cnt": 82,
        "product_id": "514410"
      },
      {
        "cnt": 82,
        "product_id": "368980"
      },
      {
        "cnt": 83,
        "product_id": "329040"
      },
      {
        "cnt": 83,
        "product_id": "246880"
      },
      {
        "cnt": 84,
        "product_id": "247310"
      },
      {
        "cnt": 84,
        "product_id": "510930"
      },
      {
        "cnt": 85,
        "product_id": "698260"
      },
      {
        "cnt": 85,
        "product_id": "463920"
      },
      {
        "cnt": 86,
        "product_id": "386600"
      },
      {
        "cnt": 86,
        "product_id": "600460"
      },
      {
        "cnt": 86,
        "product_id": "679270"
      },
      {
        "cnt": 87,
        "product_id": "448640"
      },
      {
        "cnt": 87,
        "product_id": "516590"
      },
      {
        "cnt": 87,
        "product_id": "517670"
      },
      {
        "cnt": 88,
        "product_id": "586950"
      },
      {
        "cnt": 88,
        "product_id": "263040"
      },
      {
        "cnt": 89,
        "product_id": "290810"
      },
      {
        "cnt": 89,
        "product_id": "454680"
      },
      {
        "cnt": 89,
        "product_id": "415010"
      },
      {
        "cnt": 89,
        "product_id": "534000"
      },
      {
        "cnt": 89,
        "product_id": "308600"
      },
      {
        "cnt": 89,
        "product_id": "622470"
      },
      {
        "cnt": 89,
        "product_id": "454140"
      },
      {
        "cnt": 90,
        "product_id": "566240"
      },
      {
        "cnt": 90,
        "product_id": "755770"
      },
      {
        "cnt": 91,
        "product_id": "444690"
      },
      {
        "cnt": 91,
        "product_id": "426930"
      },
      {
        "cnt": 92,
        "product_id": "503370"
      },
      {
        "cnt": 92,
        "product_id": "393790"
      },
      {
        "cnt": 92,
        "product_id": "636970"
      },
      {
        "cnt": 92,
        "product_id": "735850"
      },
      {
        "cnt": 93,
        "product_id": "317730"
      },
      {
        "cnt": 93,
        "product_id": "542700"
      },
      {
        "cnt": 93,
        "product_id": "556640"
      },
      {
        "cnt": 93,
        "product_id": "513590"
      },
      {
        "cnt": 94,
        "product_id": "450700"
      },
      {
        "cnt": 94,
        "product_id": "393390"
      },
      {
        "cnt": 94,
        "product_id": "758190"
      },
      {
        "cnt": 94,
        "product_id": "397160"
      },
      {
        "cnt": 95,
        "product_id": "432250"
      },
      {
        "cnt": 96,
        "product_id": "487250"
      },
      {
        "cnt": 96,
        "product_id": "369560"
      },
      {
        "cnt": 96,
        "product_id": "689700"
      },
      {
        "cnt": 96,
        "product_id": "335850"
      },
      {
        "cnt": 96,
        "product_id": "591790"
      },
      {
        "cnt": 97,
        "product_id": "328510"
      },
      {
        "cnt": 97,
        "product_id": "756360"
      },
      {
        "cnt": 97,
        "product_id": "531530"
      },
      {
        "cnt": 99,
        "product_id": "444460"
      },
      {
        "cnt": 99,
        "product_id": "574980"
      },
      {
        "cnt": 99,
        "product_id": "420550"
      },
      {
        "cnt": 100,
        "product_id": "266370"
      },
      {
        "cnt": 101,
        "product_id": "461210"
      },
      {
        "cnt": 101,
        "product_id": "629220"
      },
      {
        "cnt": 102,
        "product_id": "490990"
      },
      {
        "cnt": 103,
        "product_id": "690040"
      },
      {
        "cnt": 104,
        "product_id": "461400"
      },
      {
        "cnt": 104,
        "product_id": "305510"
      },
      {
        "cnt": 104,
        "product_id": "409340"
      },
      {
        "cnt": 104,
        "product_id": "300760"
      },
      {
        "cnt": 105,
        "product_id": "315540"
      },
      {
        "cnt": 105,
        "product_id": "437610"
      },
      {
        "cnt": 105,
        "product_id": "661920"
      },
      {
        "cnt": 105,
        "product_id": "640150"
      },
      {
        "cnt": 106,
        "product_id": "691390"
      },
      {
        "cnt": 106,
        "product_id": "384960"
      },
      {
        "cnt": 106,
        "product_id": "598690"
      },
      {
        "cnt": 107,
        "product_id": "328710"
      },
      {
        "cnt": 107,
        "product_id": "650350"
      },
      {
        "cnt": 108,
        "product_id": "655780"
      },
      {
        "cnt": 108,
        "product_id": "379420"
      },
      {
        "cnt": 108,
        "product_id": "525680"
      },
      {
        "cnt": 108,
        "product_id": "704830"
      },
      {
        "cnt": 108,
        "product_id": "562230"
      },
      {
        "cnt": 109,
        "product_id": "308080"
      },
      {
        "cnt": 109,
        "product_id": "636690"
      },
      {
        "cnt": 109,
        "product_id": "404550"
      },
      {
        "cnt": 110,
        "product_id": "551170"
      },
      {
        "cnt": 112,
        "product_id": "448570"
      },
      {
        "cnt": 113,
        "product_id": "408900"
      },
      {
        "cnt": 114,
        "product_id": "740290"
      },
      {
        "cnt": 116,
        "product_id": "582330"
      },
      {
        "cnt": 116,
        "product_id": "315070"
      },
      {
        "cnt": 118,
        "product_id": "524380"
      },
      {
        "cnt": 119,
        "product_id": "382480"
      },
      {
        "cnt": 119,
        "product_id": "638000"
      },
      {
        "cnt": 120,
        "product_id": "517720"
      },
      {
        "cnt": 120,
        "product_id": "298280"
      },
      {
        "cnt": 121,
        "product_id": "372750"
      },
      {
        "cnt": 121,
        "product_id": "578210"
      },
      {
        "cnt": 121,
        "product_id": "386650"
      },
      {
        "cnt": 122,
        "product_id": "534780"
      },
      {
        "cnt": 122,
        "product_id": "679400"
      },
      {
        "cnt": 122,
        "product_id": "451600"
      },
      {
        "cnt": 123,
        "product_id": "422940"
      },
      {
        "cnt": 124,
        "product_id": "555400"
      },
      {
        "cnt": 125,
        "product_id": "439370"
      },
      {
        "cnt": 125,
        "product_id": "468820"
      },
      {
        "cnt": 125,
        "product_id": "391520"
      },
      {
        "cnt": 125,
        "product_id": "437890"
      },
      {
        "cnt": 126,
        "product_id": "468070"
      },
      {
        "cnt": 127,
        "product_id": "513330"
      },
      {
        "cnt": 128,
        "product_id": "418620"
      },
      {
        "cnt": 128,
        "product_id": "414120"
      },
      {
        "cnt": 128,
        "product_id": "350150"
      },
      {
        "cnt": 131,
        "product_id": "617030"
      },
      {
        "cnt": 131,
        "product_id": "717790"
      },
      {
        "cnt": 134,
        "product_id": "266190"
      },
      {
        "cnt": 135,
        "product_id": "643810"
      },
      {
        "cnt": 136,
        "product_id": "341710"
      },
      {
        "cnt": 136,
        "product_id": "363950"
      },
      {
        "cnt": 136,
        "product_id": "384090"
      },
      {
        "cnt": 137,
        "product_id": "333340"
      },
      {
        "cnt": 137,
        "product_id": "574070"
      },
      {
        "cnt": 138,
        "product_id": "366290"
      },
      {
        "cnt": 138,
        "product_id": "611160"
      },
      {
        "cnt": 138,
        "product_id": "565030"
      },
      {
        "cnt": 139,
        "product_id": "703840"
      },
      {
        "cnt": 139,
        "product_id": "617480"
      },
      {
        "cnt": 140,
        "product_id": "654690"
      },
      {
        "cnt": 140,
        "product_id": "525610"
      },
      {
        "cnt": 141,
        "product_id": "656530"
      },
      {
        "cnt": 141,
        "product_id": "614860"
      },
      {
        "cnt": 142,
        "product_id": "422860"
      },
      {
        "cnt": 142,
        "product_id": "573490"
      },
      {
        "cnt": 142,
        "product_id": "685420"
      },
      {
        "cnt": 142,
        "product_id": "491470"
      },
      {
        "cnt": 144,
        "product_id": "324190"
      },
      {
        "cnt": 144,
        "product_id": "297310"
      },
      {
        "cnt": 144,
        "product_id": "269350"
      },
      {
        "cnt": 146,
        "product_id": "531660"
      },
      {
        "cnt": 146,
        "product_id": "546980"
      },
      {
        "cnt": 147,
        "product_id": "487000"
      },
      {
        "cnt": 147,
        "product_id": "389050"
      },
      {
        "cnt": 147,
        "product_id": "450860"
      },
      {
        "cnt": 148,
        "product_id": "621880"
      },
      {
        "cnt": 150,
        "product_id": "347170"
      },
      {
        "cnt": 152,
        "product_id": "418910"
      },
      {
        "cnt": 152,
        "product_id": "366000"
      },
      {
        "cnt": 153,
        "product_id": "369530"
      },
      {
        "cnt": 154,
        "product_id": "551700"
      },
      {
        "cnt": 154,
        "product_id": "595430"
      },
      {
        "cnt": 155,
        "product_id": "704030"
      },
      {
        "cnt": 155,
        "product_id": "329190"
      },
      {
        "cnt": 156,
        "product_id": "372820"
      },
      {
        "cnt": 157,
        "product_id": "352430"
      },
      {
        "cnt": 157,
        "product_id": "373750"
      },
      {
        "cnt": 158,
        "product_id": "458830"
      },
      {
        "cnt": 158,
        "product_id": "323670"
      },
      {
        "cnt": 159,
        "product_id": "614630"
      },
      {
        "cnt": 161,
        "product_id": "259450"
      },
      {
        "cnt": 161,
        "product_id": "390560"
      },
      {
        "cnt": 162,
        "product_id": "585420"
      },
      {
        "cnt": 163,
        "product_id": "418110"
      },
      {
        "cnt": 163,
        "product_id": "584890"
      },
      {
        "cnt": 163,
        "product_id": "569770"
      },
      {
        "cnt": 164,
        "product_id": "738500"
      },
      {
        "cnt": 164,
        "product_id": "403590"
      },
      {
        "cnt": 165,
        "product_id": "605450"
      },
      {
        "cnt": 165,
        "product_id": "305840"
      },
      {
        "cnt": 165,
        "product_id": "679260"
      },
      {
        "cnt": 166,
        "product_id": "698640"
      },
      {
        "cnt": 167,
        "product_id": "324470"
      },
      {
        "cnt": 167,
        "product_id": "718650"
      },
      {
        "cnt": 168,
        "product_id": "392080"
      },
      {
        "cnt": 168,
        "product_id": "669320"
      },
      {
        "cnt": 168,
        "product_id": "641960"
      },
      {
        "cnt": 169,
        "product_id": "416020"
      },
      {
        "cnt": 170,
        "product_id": "473910"
      },
      {
        "cnt": 170,
        "product_id": "269590"
      },
      {
        "cnt": 171,
        "product_id": "360620"
      },
      {
        "cnt": 174,
        "product_id": "462100"
      },
      {
        "cnt": 175,
        "product_id": "485900"
      },
      {
        "cnt": 175,
        "product_id": "368720"
      },
      {
        "cnt": 175,
        "product_id": "344820"
      },
      {
        "cnt": 176,
        "product_id": "757240"
      },
      {
        "cnt": 178,
        "product_id": "291370"
      },
      {
        "cnt": 180,
        "product_id": "381750"
      },
      {
        "cnt": 182,
        "product_id": "345430"
      },
      {
        "cnt": 183,
        "product_id": "415590"
      },
      {
        "cnt": 183,
        "product_id": "446120"
      },
      {
        "cnt": 184,
        "product_id": "658630"
      },
      {
        "cnt": 184,
        "product_id": "542770"
      },
      {
        "cnt": 185,
        "product_id": "568580"
      },
      {
        "cnt": 188,
        "product_id": "519080"
      },
      {
        "cnt": 189,
        "product_id": "465200"
      },
      {
        "cnt": 190,
        "product_id": "413110"
      },
      {
        "cnt": 190,
        "product_id": "339440"
      },
      {
        "cnt": 191,
        "product_id": "336440"
      },
      {
        "cnt": 191,
        "product_id": "358080"
      },
      {
        "cnt": 192,
        "product_id": "269610"
      },
      {
        "cnt": 192,
        "product_id": "616250"
      },
      {
        "cnt": 196,
        "product_id": "466980"
      },
      {
        "cnt": 197,
        "product_id": "268670"
      },
      {
        "cnt": 197,
        "product_id": "351630"
      },
      {
        "cnt": 197,
        "product_id": "276870"
      },
      {
        "cnt": 198,
        "product_id": "608110"
      },
      {
        "cnt": 198,
        "product_id": "369080"
      },
      {
        "cnt": 199,
        "product_id": "321830"
      },
      {
        "cnt": 200,
        "product_id": "503770"
      },
      {
        "cnt": 201,
        "product_id": "492340"
      },
      {
        "cnt": 201,
        "product_id": "511090"
      },
      {
        "cnt": 202,
        "product_id": "293480"
      },
      {
        "cnt": 202,
        "product_id": "280720"
      },
      {
        "cnt": 205,
        "product_id": "545050"
      },
      {
        "cnt": 207,
        "product_id": "370060"
      },
      {
        "cnt": 207,
        "product_id": "458520"
      },
      {
        "cnt": 208,
        "product_id": "622040"
      },
      {
        "cnt": 215,
        "product_id": "685690"
      },
      {
        "cnt": 215,
        "product_id": "686680"
      },
      {
        "cnt": 218,
        "product_id": "686200"
      },
      {
        "cnt": 218,
        "product_id": "612720"
      },
      {
        "cnt": 220,
        "product_id": "285380"
      },
      {
        "cnt": 220,
        "product_id": "621070"
      },
      {
        "cnt": 220,
        "product_id": "657240"
      },
      {
        "cnt": 221,
        "product_id": "377060"
      },
      {
        "cnt": 222,
        "product_id": "496250"
      },
      {
        "cnt": 223,
        "product_id": "347600"
      },
      {
        "cnt": 227,
        "product_id": "528550"
      },
      {
        "cnt": 229,
        "product_id": "257930"
      },
      {
        "cnt": 230,
        "product_id": "412130"
      },
      {
        "cnt": 235,
        "product_id": "412310"
      },
      {
        "cnt": 235,
        "product_id": "508790"
      },
      {
        "cnt": 236,
        "product_id": "297470"
      },
      {
        "cnt": 236,
        "product_id": "431450"
      },
      {
        "cnt": 236,
        "product_id": "529240"
      },
      {
        "cnt": 239,
        "product_id": "642390"
      },
      {
        "cnt": 239,
        "product_id": "608990"
      },
      {
        "cnt": 240,
        "product_id": "552620"
      },
      {
        "cnt": 241,
        "product_id": "553660"
      },
      {
        "cnt": 243,
        "product_id": "672630"
      },
      {
        "cnt": 245,
        "product_id": "505060"
      },
      {
        "cnt": 247,
        "product_id": "315330"
      },
      {
        "cnt": 247,
        "product_id": "481870"
      },
      {
        "cnt": 247,
        "product_id": "283100"
      },
      {
        "cnt": 250,
        "product_id": "663300"
      },
      {
        "cnt": 250,
        "product_id": "552920"
      },
      {
        "cnt": 251,
        "product_id": "611800"
      },
      {
        "cnt": 251,
        "product_id": "638850"
      },
      {
        "cnt": 252,
        "product_id": "292330"
      },
      {
        "cnt": 253,
        "product_id": "719590"
      },
      {
        "cnt": 253,
        "product_id": "467570"
      },
      {
        "cnt": 259,
        "product_id": "330460"
      },
      {
        "cnt": 260,
        "product_id": "695690"
      },
      {
        "cnt": 261,
        "product_id": "528460"
      },
      {
        "cnt": 262,
        "product_id": "671440"
      },
      {
        "cnt": 263,
        "product_id": "307090"
      },
      {
        "cnt": 264,
        "product_id": "427950"
      },
      {
        "cnt": 264,
        "product_id": "492150"
      },
      {
        "cnt": 266,
        "product_id": "346970"
      },
      {
        "cnt": 266,
        "product_id": "451650"
      },
      {
        "cnt": 267,
        "product_id": "382000"
      },
      {
        "cnt": 267,
        "product_id": "649900"
      },
      {
        "cnt": 267,
        "product_id": "448850"
      },
      {
        "cnt": 267,
        "product_id": "706020"
      },
      {
        "cnt": 270,
        "product_id": "601540"
      },
      {
        "cnt": 270,
        "product_id": "468920"
      },
      {
        "cnt": 273,
        "product_id": "681390"
      },
      {
        "cnt": 274,
        "product_id": "512220"
      },
      {
        "cnt": 274,
        "product_id": "350220"
      },
      {
        "cnt": 276,
        "product_id": "347940"
      },
      {
        "cnt": 279,
        "product_id": "402160"
      },
      {
        "cnt": 280,
        "product_id": "600120"
      },
      {
        "cnt": 281,
        "product_id": "592260"
      },
      {
        "cnt": 282,
        "product_id": "428080"
      },
      {
        "cnt": 282,
        "product_id": "681280"
      },
      {
        "cnt": 284,
        "product_id": "282880"
      },
      {
        "cnt": 284,
        "product_id": "488550"
      },
      {
        "cnt": 287,
        "product_id": "476700"
      },
      {
        "cnt": 293,
        "product_id": "299420"
      },
      {
        "cnt": 294,
        "product_id": "263920"
      },
      {
        "cnt": 296,
        "product_id": "439340"
      },
      {
        "cnt": 296,
        "product_id": "728730"
      },
      {
        "cnt": 297,
        "product_id": "582890"
      },
      {
        "cnt": 297,
        "product_id": "508550"
      },
      {
        "cnt": 297,
        "product_id": "552080"
      },
      {
        "cnt": 304,
        "product_id": "321980"
      },
      {
        "cnt": 305,
        "product_id": "464470"
      },
      {
        "cnt": 305,
        "product_id": "722730"
      },
      {
        "cnt": 305,
        "product_id": "416670"
      },
      {
        "cnt": 307,
        "product_id": "311800"
      },
      {
        "cnt": 309,
        "product_id": "263720"
      },
      {
        "cnt": 313,
        "product_id": "466220"
      },
      {
        "cnt": 315,
        "product_id": "552110"
      },
      {
        "cnt": 317,
        "product_id": "696370"
      },
      {
        "cnt": 319,
        "product_id": "564050"
      },
      {
        "cnt": 321,
        "product_id": "670160"
      },
      {
        "cnt": 324,
        "product_id": "496500"
      },
      {
        "cnt": 325,
        "product_id": "566860"
      },
      {
        "cnt": 326,
        "product_id": "465490"
      },
      {
        "cnt": 330,
        "product_id": "667970"
      },
      {
        "cnt": 332,
        "product_id": "442210"
      },
      {
        "cnt": 336,
        "product_id": "686260"
      },
      {
        "cnt": 336,
        "product_id": "504300"
      },
      {
        "cnt": 338,
        "product_id": "594650"
      },
      {
        "cnt": 340,
        "product_id": "329970"
      },
      {
        "cnt": 343,
        "product_id": "428180"
      },
      {
        "cnt": 344,
        "product_id": "462440"
      },
      {
        "cnt": 348,
        "product_id": "457010"
      },
      {
        "cnt": 352,
        "product_id": "604240"
      },
      {
        "cnt": 355,
        "product_id": "433170"
      },
      {
        "cnt": 357,
        "product_id": "616720"
      },
      {
        "cnt": 358,
        "product_id": "414070"
      },
      {
        "cnt": 363,
        "product_id": "379210"
      },
      {
        "cnt": 370,
        "product_id": "427880"
      },
      {
        "cnt": 370,
        "product_id": "570980"
      },
      {
        "cnt": 373,
        "product_id": "489380"
      },
      {
        "cnt": 377,
        "product_id": "252770"
      },
      {
        "cnt": 379,
        "product_id": "315840"
      },
      {
        "cnt": 382,
        "product_id": "420930"
      },
      {
        "cnt": 388,
        "product_id": "520860"
      },
      {
        "cnt": 389,
        "product_id": "525640"
      },
      {
        "cnt": 390,
        "product_id": "339910"
      },
      {
        "cnt": 392,
        "product_id": "325210"
      },
      {
        "cnt": 394,
        "product_id": "442710"
      },
      {
        "cnt": 396,
        "product_id": "272230"
      },
      {
        "cnt": 403,
        "product_id": "332650"
      },
      {
        "cnt": 405,
        "product_id": "489460"
      },
      {
        "cnt": 411,
        "product_id": "562270"
      },
      {
        "cnt": 412,
        "product_id": "305940"
      },
      {
        "cnt": 428,
        "product_id": "246300"
      },
      {
        "cnt": 428,
        "product_id": "466110"
      },
      {
        "cnt": 431,
        "product_id": "414080"
      },
      {
        "cnt": 432,
        "product_id": "393930"
      },
      {
        "cnt": 438,
        "product_id": "612470"
      },
      {
        "cnt": 438,
        "product_id": "570460"
      },
      {
        "cnt": 439,
        "product_id": "335620"
      },
      {
        "cnt": 449,
        "product_id": "576470"
      },
      {
        "cnt": 449,
        "product_id": "591370"
      },
      {
        "cnt": 450,
        "product_id": "632300"
      },
      {
        "cnt": 453,
        "product_id": "381180"
      },
      {
        "cnt": 456,
        "product_id": "330570"
      },
      {
        "cnt": 457,
        "product_id": "15540"
      },
      {
        "cnt": 465,
        "product_id": "530560"
      },
      {
        "cnt": 469,
        "product_id": "397150"
      },
      {
        "cnt": 486,
        "product_id": "520010"
      },
      {
        "cnt": 492,
        "product_id": "385890"
      },
      {
        "cnt": 499,
        "product_id": "623880"
      },
      {
        "cnt": 499,
        "product_id": "746930"
      },
      {
        "cnt": 500,
        "product_id": "666020"
      },
      {
        "cnt": 501,
        "product_id": "422420"
      },
      {
        "cnt": 505,
        "product_id": "658980"
      },
      {
        "cnt": 505,
        "product_id": "406090"
      },
      {
        "cnt": 509,
        "product_id": "285110"
      },
      {
        "cnt": 512,
        "product_id": "351100"
      },
      {
        "cnt": 516,
        "product_id": "486690"
      },
      {
        "cnt": 527,
        "product_id": "251890"
      },
      {
        "cnt": 540,
        "product_id": "423890"
      },
      {
        "cnt": 541,
        "product_id": "494150"
      },
      {
        "cnt": 548,
        "product_id": "748370"
      },
      {
        "cnt": 549,
        "product_id": "342310"
      },
      {
        "cnt": 553,
        "product_id": "357330"
      },
      {
        "cnt": 574,
        "product_id": "598700"
      },
      {
        "cnt": 575,
        "product_id": "405010"
      },
      {
        "cnt": 578,
        "product_id": "368860"
      },
      {
        "cnt": 580,
        "product_id": "263200"
      },
      {
        "cnt": 599,
        "product_id": "690510"
      },
      {
        "cnt": 599,
        "product_id": "325420"
      },
      {
        "cnt": 606,
        "product_id": "377140"
      },
      {
        "cnt": 609,
        "product_id": "417290"
      },
      {
        "cnt": 614,
        "product_id": "612930"
      },
      {
        "cnt": 624,
        "product_id": "574760"
      },
      {
        "cnt": 626,
        "product_id": "363490"
      },
      {
        "cnt": 626,
        "product_id": "574080"
      },
      {
        "cnt": 629,
        "product_id": "499660"
      },
      {
        "cnt": 632,
        "product_id": "363360"
      },
      {
        "cnt": 633,
        "product_id": "305960"
      },
      {
        "cnt": 639,
        "product_id": "274620"
      },
      {
        "cnt": 644,
        "product_id": "587450"
      },
      {
        "cnt": 657,
        "product_id": "467820"
      },
      {
        "cnt": 662,
        "product_id": "470600"
      },
      {
        "cnt": 665,
        "product_id": "410340"
      },
      {
        "cnt": 665,
        "product_id": "340810"
      },
      {
        "cnt": 676,
        "product_id": "382310"
      },
      {
        "cnt": 689,
        "product_id": "504050"
      },
      {
        "cnt": 690,
        "product_id": "412470"
      },
      {
        "cnt": 694,
        "product_id": "324510"
      },
      {
        "cnt": 695,
        "product_id": "455980"
      },
      {
        "cnt": 698,
        "product_id": "356510"
      },
      {
        "cnt": 700,
        "product_id": "572520"
      },
      {
        "cnt": 706,
        "product_id": "562500"
      },
      {
        "cnt": 713,
        "product_id": "619080"
      },
      {
        "cnt": 722,
        "product_id": "576770"
      },
      {
        "cnt": 736,
        "product_id": "463530"
      },
      {
        "cnt": 740,
        "product_id": "454150"
      },
      {
        "cnt": 750,
        "product_id": "521150"
      },
      {
        "cnt": 774,
        "product_id": "252250"
      },
      {
        "cnt": 777,
        "product_id": "259570"
      },
      {
        "cnt": 786,
        "product_id": "370770"
      },
      {
        "cnt": 789,
        "product_id": "223490"
      },
      {
        "cnt": 799,
        "product_id": "397100"
      },
      {
        "cnt": 815,
        "product_id": "405710"
      },
      {
        "cnt": 821,
        "product_id": "293220"
      },
      {
        "cnt": 832,
        "product_id": "537340"
      },
      {
        "cnt": 840,
        "product_id": "385380"
      },
      {
        "cnt": 841,
        "product_id": "577230"
      },
      {
        "cnt": 842,
        "product_id": "598960"
      },
      {
        "cnt": 849,
        "product_id": "312210"
      },
      {
        "cnt": 850,
        "product_id": "277930"
      },
      {
        "cnt": 873,
        "product_id": "544550"
      },
      {
        "cnt": 877,
        "product_id": "519860"
      },
      {
        "cnt": 889,
        "product_id": "550840"
      },
      {
        "cnt": 910,
        "product_id": "375480"
      },
      {
        "cnt": 912,
        "product_id": "586030"
      },
      {
        "cnt": 921,
        "product_id": "280010"
      },
      {
        "cnt": 943,
        "product_id": "527430"
      },
      {
        "cnt": 960,
        "product_id": "461430"
      },
      {
        "cnt": 963,
        "product_id": "656200"
      },
      {
        "cnt": 965,
        "product_id": "374670"
      },
      {
        "cnt": 983,
        "product_id": "604490"
      },
      {
        "cnt": 990,
        "product_id": "347560"
      },
      {
        "cnt": 999,
        "product_id": "520530"
      },
      {
        "cnt": 1007,
        "product_id": "312150"
      },
      {
        "cnt": 1019,
        "product_id": "322300"
      },
      {
        "cnt": 1020,
        "product_id": "734580"
      },
      {
        "cnt": 1021,
        "product_id": "429050"
      },
      {
        "cnt": 1044,
        "product_id": "307110"
      },
      {
        "cnt": 1045,
        "product_id": "333640"
      },
      {
        "cnt": 1048,
        "product_id": "314230"
      },
      {
        "cnt": 1060,
        "product_id": "396900"
      },
      {
        "cnt": 1061,
        "product_id": "248630"
      },
      {
        "cnt": 1064,
        "product_id": "541300"
      },
      {
        "cnt": 1067,
        "product_id": "597170"
      },
      {
        "cnt": 1080,
        "product_id": "293760"
      },
      {
        "cnt": 1101,
        "product_id": "285580"
      },
      {
        "cnt": 1121,
        "product_id": "409590"
      },
      {
        "cnt": 1125,
        "product_id": "415860"
      },
      {
        "cnt": 1135,
        "product_id": "328080"
      },
      {
        "cnt": 1139,
        "product_id": "453090"
      },
      {
        "cnt": 1139,
        "product_id": "375530"
      },
      {
        "cnt": 1149,
        "product_id": "466860"
      },
      {
        "cnt": 1155,
        "product_id": "327640"
      },
      {
        "cnt": 1159,
        "product_id": "342560"
      },
      {
        "cnt": 1165,
        "product_id": "673610"
      },
      {
        "cnt": 1168,
        "product_id": "488440"
      },
      {
        "cnt": 1171,
        "product_id": "555160"
      },
      {
        "cnt": 1177,
        "product_id": "533120"
      },
      {
        "cnt": 1186,
        "product_id": "385270"
      },
      {
        "cnt": 1192,
        "product_id": "340150"
      },
      {
        "cnt": 1194,
        "product_id": "606800"
      },
      {
        "cnt": 1223,
        "product_id": "538100"
      },
      {
        "cnt": 1230,
        "product_id": "454350"
      },
      {
        "cnt": 1256,
        "product_id": "330580"
      },
      {
        "cnt": 1270,
        "product_id": "332570"
      },
      {
        "cnt": 1272,
        "product_id": "607200"
      },
      {
        "cnt": 1294,
        "product_id": "547680"
      },
      {
        "cnt": 1294,
        "product_id": "559650"
      },
      {
        "cnt": 1295,
        "product_id": "598330"
      },
      {
        "cnt": 1295,
        "product_id": "469600"
      },
      {
        "cnt": 1302,
        "product_id": "671510"
      },
      {
        "cnt": 1312,
        "product_id": "357770"
      },
      {
        "cnt": 1314,
        "product_id": "322780"
      },
      {
        "cnt": 1340,
        "product_id": "326160"
      },
      {
        "cnt": 1373,
        "product_id": "366090"
      },
      {
        "cnt": 1390,
        "product_id": "227780"
      },
      {
        "cnt": 1399,
        "product_id": "611790"
      },
      {
        "cnt": 1414,
        "product_id": "389040"
      },
      {
        "cnt": 1452,
        "product_id": "375510"
      },
      {
        "cnt": 1473,
        "product_id": "367270"
      },
      {
        "cnt": 1507,
        "product_id": "627690"
      },
      {
        "cnt": 1527,
        "product_id": "412450"
      },
      {
        "cnt": 1535,
        "product_id": "485310"
      },
      {
        "cnt": 1565,
        "product_id": "450540"
      },
      {
        "cnt": 1566,
        "product_id": "321400"
      },
      {
        "cnt": 1569,
        "product_id": "449960"
      },
      {
        "cnt": 1570,
        "product_id": "251950"
      },
      {
        "cnt": 1584,
        "product_id": "568220"
      },
      {
        "cnt": 1597,
        "product_id": "578620"
      },
      {
        "cnt": 1640,
        "product_id": "518030"
      },
      {
        "cnt": 1669,
        "product_id": "331360"
      },
      {
        "cnt": 1686,
        "product_id": "700030"
      },
      {
        "cnt": 1724,
        "product_id": "588210"
      },
      {
        "cnt": 1815,
        "product_id": "509980"
      },
      {
        "cnt": 1828,
        "product_id": "302590"
      },
      {
        "cnt": 1836,
        "product_id": "552100"
      },
      {
        "cnt": 1841,
        "product_id": "252870"
      },
      {
        "cnt": 1879,
        "product_id": "318100"
      },
      {
        "cnt": 1906,
        "product_id": "571740"
      },
      {
        "cnt": 1932,
        "product_id": "311260"
      },
      {
        "cnt": 1937,
        "product_id": "298610"
      },
      {
        "cnt": 1939,
        "product_id": "773951"
      },
      {
        "cnt": 1971,
        "product_id": "374280"
      },
      {
        "cnt": 1983,
        "product_id": "372800"
      },
      {
        "cnt": 2007,
        "product_id": "224440"
      },
      {
        "cnt": 2051,
        "product_id": "252850"
      },
      {
        "cnt": 2084,
        "product_id": "327090"
      },
      {
        "cnt": 2088,
        "product_id": "424370"
      },
      {
        "cnt": 2133,
        "product_id": "322770"
      },
      {
        "cnt": 2164,
        "product_id": "362620"
      },
      {
        "cnt": 2287,
        "product_id": "327070"
      },
      {
        "cnt": 2304,
        "product_id": "471710"
      },
      {
        "cnt": 2366,
        "product_id": "496240"
      },
      {
        "cnt": 2413,
        "product_id": "527230"
      },
      {
        "cnt": 2451,
        "product_id": "244770"
      },
      {
        "cnt": 2491,
        "product_id": "418030"
      },
      {
        "cnt": 2520,
        "product_id": "315460"
      },
      {
        "cnt": 2550,
        "product_id": "445220"
      },
      {
        "cnt": 2582,
        "product_id": "324080"
      },
      {
        "cnt": 2697,
        "product_id": "368340"
      },
      {
        "cnt": 2790,
        "product_id": "446020"
      },
      {
        "cnt": 2791,
        "product_id": "531640"
      },
      {
        "cnt": 2806,
        "product_id": "666140"
      },
      {
        "cnt": 2817,
        "product_id": "589290"
      },
      {
        "cnt": 2836,
        "product_id": "320240"
      },
      {
        "cnt": 2841,
        "product_id": "362490"
      },
      {
        "cnt": 2843,
        "product_id": "526160"
      },
      {
        "cnt": 2962,
        "product_id": "378370"
      },
      {
        "cnt": 2964,
        "product_id": "487120"
      },
      {
        "cnt": 2983,
        "product_id": "429790"
      },
      {
        "cnt": 3033,
        "product_id": "346330"
      },
      {
        "cnt": 3098,
        "product_id": "269770"
      },
      {
        "cnt": 3101,
        "product_id": "457330"
      },
      {
        "cnt": 3299,
        "product_id": "233610"
      },
      {
        "cnt": 3426,
        "product_id": "581630"
      },
      {
        "cnt": 3435,
        "product_id": "337950"
      },
      {
        "cnt": 3475,
        "product_id": "285920"
      },
      {
        "cnt": 3626,
        "product_id": "344040"
      },
      {
        "cnt": 3752,
        "product_id": "268650"
      },
      {
        "cnt": 3883,
        "product_id": "512900"
      },
      {
        "cnt": 3919,
        "product_id": "233860"
      },
      {
        "cnt": 3927,
        "product_id": "611500"
      },
      {
        "cnt": 3930,
        "product_id": "291860"
      },
      {
        "cnt": 4035,
        "product_id": "333950"
      },
      {
        "cnt": 4056,
        "product_id": "302670"
      },
      {
        "cnt": 4176,
        "product_id": "394690"
      },
      {
        "cnt": 4180,
        "product_id": "311310"
      },
      {
        "cnt": 4351,
        "product_id": "505460"
      },
      {
        "cnt": 4550,
        "product_id": "337320"
      },
      {
        "cnt": 4699,
        "product_id": "230290"
      },
      {
        "cnt": 4869,
        "product_id": "489520"
      },
      {
        "cnt": 4964,
        "product_id": "253250"
      },
      {
        "cnt": 5191,
        "product_id": "636480"
      },
      {
        "cnt": 5406,
        "product_id": "558100"
      },
      {
        "cnt": 5496,
        "product_id": "307880"
      },
      {
        "cnt": 5652,
        "product_id": "644560"
      },
      {
        "cnt": 5735,
        "product_id": "519190"
      },
      {
        "cnt": 5930,
        "product_id": "332500"
      },
      {
        "cnt": 5981,
        "product_id": "489940"
      },
      {
        "cnt": 6233,
        "product_id": "646570"
      },
      {
        "cnt": 6422,
        "product_id": "376210"
      },
      {
        "cnt": 6470,
        "product_id": "232810"
      },
      {
        "cnt": 6689,
        "product_id": "529180"
      },
      {
        "cnt": 7214,
        "product_id": "351290"
      },
      {
        "cnt": 7362,
        "product_id": "236370"
      },
      {
        "cnt": 7534,
        "product_id": "228380"
      },
      {
        "cnt": 7636,
        "product_id": "644930"
      },
      {
        "cnt": 7705,
        "product_id": "402710"
      },
      {
        "cnt": 8041,
        "product_id": "516750"
      },
      {
        "cnt": 8045,
        "product_id": "466560"
      },
      {
        "cnt": 8056,
        "product_id": "206500"
      },
      {
        "cnt": 8695,
        "product_id": "326460"
      },
      {
        "cnt": 9201,
        "product_id": "457140"
      },
      {
        "cnt": 9696,
        "product_id": "362890"
      },
      {
        "cnt": 9748,
        "product_id": "383120"
      },
      {
        "cnt": 9772,
        "product_id": "284160"
      },
      {
        "cnt": 9876,
        "product_id": "244930"
      },
      {
        "cnt": 10762,
        "product_id": "431240"
      },
      {
        "cnt": 11566,
        "product_id": "588650"
      },
      {
        "cnt": 12503,
        "product_id": "438100"
      },
      {
        "cnt": 13445,
        "product_id": "387990"
      },
      {
        "cnt": 13912,
        "product_id": "391460"
      },
      {
        "cnt": 15470,
        "product_id": "440900"
      },
      {
        "cnt": 15486,
        "product_id": "108600"
      },
      {
        "cnt": 16326,
        "product_id": "355840"
      },
      {
        "cnt": 16797,
        "product_id": "393420"
      },
      {
        "cnt": 17269,
        "product_id": "294100"
      },
      {
        "cnt": 17833,
        "product_id": "393380"
      },
      {
        "cnt": 18183,
        "product_id": "313120"
      },
      {
        "cnt": 18724,
        "product_id": "361420"
      },
      {
        "cnt": 20047,
        "product_id": "550650"
      },
      {
        "cnt": 21650,
        "product_id": "346010"
      },
      {
        "cnt": 21738,
        "product_id": "299740"
      },
      {
        "cnt": 24286,
        "product_id": "302830"
      },
      {
        "cnt": 24741,
        "product_id": "427520"
      },
      {
        "cnt": 37288,
        "product_id": "431960"
      },
      {
        "cnt": 49917,
        "product_id": "244850"
      },
      {
        "cnt": 53955,
        "product_id": "251570"
      },
      {
        "cnt": 67341,
        "product_id": "295110"
      },
      {
        "cnt": 68963,
        "product_id": "242760"
      },
      {
        "cnt": 106744,
        "product_id": "444090"
      },
      {
        "cnt": 126642,
        "product_id": "433850"
      },
      {
        "cnt": 139867,
        "product_id": "221100"
      }
    ] t

    where t.product_id in
    (select raw product_id from store where user_score = """ + str(i) + ")").replace('\n', '')

    results = db.run_query(query, 'job')

    review_counts = []

    for row in results:
        review_counts.append(row['cnt'])

    overall.append(
        {
            "score": i,
            "review_count": review_counts
        }
    )

print overall