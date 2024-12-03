# run:
# curl https://raw.githubusercontent.com/mdpakk/DarkRetro2K/refs/heads/main/python/favgroup_icons_db.py | python
# and copy output to styles_*_db.css

favgroup_icons_db={
  34398:"https://cdn-icons-png.flaticon.com/512/1409/1409942.png",
  36181:"https://cdn.donmai.us/180x180/d3/0e/d30e5ca9e0604f1658e7ea8fbcc39f68.jpg",
  34399:"https://cdn.donmai.us/180x180/82/2c/822c16c429dfe7fba6a9b471c2964f10.jpg",
  36104:"https://cdn.donmai.us/180x180/7a/5a/7a5aa49f0c43aa325463b8b34140b836.jpg",
  34397:"https://cdn.donmai.us/180x180/88/82/8882ae9df5ea296a314b86eeac13d6a0.jpg",
}

for favgroup_icon in favgroup_icons_db.items():
    print(f'''tr#favorite-group-{favgroup_icon[0]} td.name-column a:first-child {{
    background-image: url({favgroup_icon[1]}) !important;
}}''')
