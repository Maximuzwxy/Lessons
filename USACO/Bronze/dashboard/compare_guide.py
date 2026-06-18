import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('data/usaco_bronze_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

db_cpids = {p['cpid'] for p in db['problems']}

# All USACO Bronze CPIDs from usaco.guide (verified above)
guide_cpids = {
    # Simulation
    665: "The Cow-Signal", 568: "Speeding Ticket", 735: "The Lost Cow", 
    760: "The Bovine Shuffle", 856: "The Bucket List",
    917: "Measuring Traffic", 616: "Circular Barn", 664: "Block Game",
    831: "Team Tic Tac Toe", 593: "Mowing the Field", 1491: "Reflection",
    526: "[OLD BRONZE] Censoring", 761: "Milk Measurement", 1061: "Stuck in a Rut",
    
    # Basic Complete Search
    615: "Milk Pails", 639: "Diamond Collector", 1060: "Daisy Chains",
    1228: "Counting Liars", 963: "Cow Gymnastics", 736: "Bovine Genomics",
    1011: "Triangles", 784: "Lifeguards", 712: "Why Did the Cow Cross the Road II",
    893: "Guess the Animal", 617: "Load Balancing", 1203: "Sleeping in Class",
    1469: "Cow Checkups", 569: "Contaminated Milk", 1037: "Cowntact Tracing",
    640: "Bull in a China Shop", 1324: "Moo Language",
    
    # Complete Search with Recursion
    1276: "Air Cownditioning II", 965: "Livestock Lineup", 857: "Back and Forth",
    1493: "Printing Sequences",
    
    # Sorting
    713: "Why Did the Cow Cross the Road III", 1251: "Cow College", 592: "Angry Cows",
    
    # Sets & Maps
    964: "Where Am I?", 1107: "Year of the Cow", 687: "Don't Be Last!",
    1468: "It's Mooin' Time II", 1445: "It's Mooin' Time",
    
    # Ad Hoc
    591: "Promotion Counting", 892: "Sleepy Cow Sorting", 809: "Taming the Herd",
    737: "Modern Art", 1204: "Photoshoot 2",
    
    # Casework
    567: "Fence Painting", 1035: "Social Distancing I", 1515: "Hoof Paper Scissors Minus One",
    1275: "Leaders", 915: "Sleepy Cow Herding",
    
    # Greedy
    1301: "Watching Mooloo", 689: "Cow Tipping", 1084: "Even More Odd Photos",
    785: "Out of Place", 1467: "Astral Superposition", 832: "Milking Order",
    1227: "Photoshoot", 1323: "FEB", 989: "Race", 1012: "Mad Scientist",
    
    # Graphs
    916: "The Great Revegetation", 940: "Milk Factory", 808: "Hoofball",
    1013: "Swapity Swap", 941: "Cow Evolution", 833: "Family Tree",
    
    # Rectangle Geometry
    663: "Square Pasture", 783: "Blocked Billboard II",
    
    # Bronze Conclusion
    1181: "Drought",
}

print("="*60)
print("CPIDs on usaco.guide but NOT in our database:")
print("="*60)
missing = []
for cpid, name in sorted(guide_cpids.items()):
    if cpid not in db_cpids:
        missing.append((cpid, name))
        print(f"  CPID {cpid}: {name}")

if not missing:
    print("  NONE - all covered!")

print(f"\nTotal on usaco.guide: {len(guide_cpids)}")
print(f"Total in our DB: {len(db_cpids)}")
print(f"Missing: {len(missing)}")

print("\n" + "="*60)
print("CPIDs in our DB but NOT on usaco.guide:")
print("="*60)
not_on_guide = []
for cpid in sorted(db_cpids):
    if cpid not in guide_cpids:
        p = [x for x in db['problems'] if x['cpid'] == cpid][0]
        not_on_guide.append((cpid, p['name']))
        if len(not_on_guide) <= 15:
            print(f"  CPID {cpid}: {p['name']}")
if len(not_on_guide) > 15:
    print(f"  ... and {len(not_on_guide)-15} more")
print(f"\nTotal only in DB: {len(not_on_guide)}")
