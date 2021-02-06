from django.http import HttpResponse
from django.shortcuts import render

items  = [{
                "thing": "ch1ck3n McNuggets",
                "price": 15,
                "about": "It's a ch1ck3n nugget and comes with a super fun mystery prize!",
                "url": "https://i.insider.com/5f5f7e5de6ff30001d4e891c?width=1136&format=jpeg",
                "id": 1,
                "recipe": "First, grab an edible ch1cl3n. fill a frying pan with oil. put tempura panko on the ch1ck3n. put eggs on it. put it in the hot boiling oil. it should fry up. when done take out."
             },
             {
                "thing": "Hot Doge",
                "price": 16,
                "about": "A fun hot dog with a doge! (note that the doge is just shaped bread)",
                "url": "https://i.pinimg.com/originals/fc/e8/42/fce8429a9bde6658141292935d90d927.jpg",
                "recipe": "First, put a sausauoge in a dogebun. then, put ketchupdoge on the sausauoge and dogebun. put doge mustard if you want.",
                "id": 2
             },
             {
                "thing": "Smore's",
                "price": 3,
                "about": "A delicious treat.",
                "url": "http://irepo.primecp.com/2015/09/236970/Smores-on-the-Grill_ExtraLarge1000_ID-1195440.jpg?v=1195440",
                "recipe": "get dogeraham cracker, a dogeshmallow, and a dogershy's chocolate. put the dogeshmallow on a stick and put it in a campfire until doge color. when doge color put it on top of dogershy's chocolate. put those two in between two dogeraham crackers. when dogeshmallow is melted you are to eat it.",
                "id": 3
             },
             {
                "thing": "McDogealds's Baconator",
                "price": 1,
                "about": "The Baconator sandwich is a cheeseburger sold by the international fast-food restaurant chain McDogealds",
                "url": "https://static.wikia.nocookie.net/bacon/images/3/3a/New_baconator.jpg/revision/latest/scale-to-width-down/340?cb=20171126021042",
                "recipe": "The Baconator is a sandwich made by McDogeald's restaurants. It has two beef patties, two slices of American cheese, six strips of bacon, mayonnaise, and ketchup on a bun.",
                "id": 4
             }]

def index(request):
    return render(request, "site/index.html")

def things(request):
    return render(request, "site/things.html", {"items": items})
def recipe(request, recipeid):
    return render(request, "site/recipe.html", {"item": items[int(recipeid)-1], "theitems": items})
