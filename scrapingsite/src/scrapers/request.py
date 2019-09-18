import requests

payload = {
    "booking": {
        "start": "2019-09-17T18:00:00",
        "end": "2019-09-17T18:30:00",
        "endOfLastOccurrence": None,
        "title": "esto es una prueba",
        "notes": "1234567890987654321",
        "price": 0,
        "chargeTransactionId": None,
        "lockInMargin": 0,
        "type": 1,
        "paymentStatus": 0,
        "recurrenceRule": None,
        "decoupleDate": None,
        "createdDate": None,
        "customFields": [],
        "piId": None,
        "arbitraryerrors": None,
        "spaces": [
            "249913"
        ],
        "venueuser": "841357",
        "venue": "87558",
        "decoupleBooking": None
    }
}

dic = {
    "cookie": "X-Skedda-RequestVerificationCookie=CfDJ8LEU-Of7Xi5JksZKiXZWccXlQCKOLyFxyqAgoYFF7COl_lj58P9Ce3PfCA9aQaEXEoQP2kGsiCr_-ubsKte71iyUZK4GbO3dhXdupPBMj4dC1TUyKmaf3oW0cuzt-7n_oHjE-hoBlmZ96o3pYggy8yg; __cfduid=d2429d0b257b5e06f083b9309cff3e7001566921954; intercom-id-7bfdd68951cfb3532964743aa3f1595669f10598=7322acb3-f532-41a8-8b4f-2ff7c3539b98; X-Skedda-ApplicationCookie=CfDJ8LEU-Of7Xi5JksZKiXZWccVRsCE_DN1-RlYvAJ0b_Bf62T79J88nuogZxrO6n25xF_yw2wjh8S6xyoTJhV_-J1WO6CxqNCBfsfPWD2duvxoSdzFhINt074i_48R_6gCRNYfF99s9ks1J3oM48bcL8J-x069BvJdVrBj5YoY6fiIsBAAtzRC2oO7Qmez1DrBUIMz2KYvnmab2V4sUSE4BGAMepujlZvSmPL-Z5e77LKG91JwdrnPmioPyP3_06wt9hUN6wQAGXNNSeR2u1aqiy77HjXGgi5YxRpzQSkgKET61TABXLriDhwZ3UR-n9tauYTqR0neNcIfvPXluyd185DOugokU32zb0X65WoJXv0D5aeLJ5MdANLqP-QKqm04g2JG_WRfqQmZuVGfoBrzVIsagi3n789buKl5j3_lTWJFIcu4d5xTIyMKy0AW2pOk-Q2Fjssl5kQgPRthJltbXeoFWg3iqkDnovp1DqATQ-x4Zmindsw6RiY3eCOmMYtDWN4LMl5cKtbXx7B-x_MTrkulZlYOTWDSpgmpRCV9VjHwUWmmxR4-zbKA1Iyn28JPdNhHRmcKxRuBTTgp80ZUm3CdqZ11npVH-Jbf94UXukDqFptCLwYKPzmRWZa9JOvpZPBl8cIch01jrtA7wPScZqcNrnmiQ9y5dFYXGUqrgvt25y5o-VUmL53Cn4m-VeiN8XbRecMgPKsZEVRG-q0CS4Fk",
    "x-skedda-requestverificationtoken": "CfDJ8LEU-Of7Xi5JksZKiXZWccW1l-8srYfQjqSDHs3hVJFbcj-eHPNzo_R4KpGo34BwSJ7h8iqWHz_qPWuBlU0e6pQn7QFMn3kvDp8CflEQgxyWBqx2ysNEBIq8hRlXJhzJZgnzwxjNYfTbfly1GekC17C-UuSa-gyMIyF-uRpEwhNeE15Cd1q6M7ZT3_YWtOasXA"
}
r = requests.post('https://teamintcol.skedda.com/bookings',json=payload,headers=dic)

print(r.json())