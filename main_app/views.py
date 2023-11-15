from django.shortcuts import render

headbands = [
  {"name": "Red Plaid Minnie Mouse Ear Headband", "material": "Cloth", "description": "Minnie brings her sparkling personality to this glamorous ear headband. The striking red plaid design features a red velvet bow studded with faceted jewels and pearlescent polka dots.", "price": 35},
  {"name": 'The Haunted Mansion "Eyes" Ear Headband', "material": "Simulated Leather", "description": "Inspired by the Disney Park attraction, it comes complete with an iconic pair of eyes acting the part of the headband's bow.", "price": 21},
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def headbands_index(request):
 return render(request, 'headbands/index.html', {
   'headbands': headbands
  })