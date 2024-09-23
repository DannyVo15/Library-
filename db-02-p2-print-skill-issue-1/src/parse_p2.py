from bs4 import BeautifulSoup

chemicals = {}
seq = 1
with open('data/p2.csv', 'wt') as f_out:
    f_out.write(f'facility_id,facility_name,facility_address,chemical,industry,year,amount\n')
    with open('data/p2.html') as f_in:
        print('Parsing...')
        total = 1
        soup = BeautifulSoup(f_in, 'html.parser')
        print('done!')
        table = soup.find('table', {'id': 'results2'})
        body = table.find('tbody')
        for tr in body.find_all('tr'):
            if total % 1000 == 0:
                print(total)
            total += 1
            td = tr.find_all('td')
            facility_id = td[0].contents[0]
            facility_name = td[1].text
            facility_address = td[2].text
            chemical_name = td[3].contents[0]
            chemical_id = seq
            if chemical_name not in chemicals:
                chemicals[chemical_name] = seq 
                seq +=1
            else:
                chemical_id = chemicals[chemical_name]
            chemical = f'{chemical_id}:{chemical_name}'
            industry = td[4].text
            year = int(td[5].contents[0]) - 1
            release = float(td[6].contents[0].replace(',', ''))
            f_out.write(f'{facility_id},"{facility_name}","{facility_address}","{chemical}","{industry}",{year},{release}\n')
