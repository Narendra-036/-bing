from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

import time
words = [
    'Demi Lovato', 'Elf film', 'Minneapolis', 'Presidential system', 'Leonard Cohen', 'Fashion design', 'Microsoft SQL Server', 'Gabriel García Márquez', 'Odyssey', 'List of colors: A-F', 'Board of directors', 'Lava', 'Sahrawi Arab Democratic Republic', 'United States Department of Defense', 'Church of England', 'Morgan Wallen', 'ITV (TV network)', 'West Bromwich Albion F.C.', 'Quantum entanglement', 'USB', 'Alphabet Inc.', 'Renault', 'ACF Fiorentina', 'Diane Lane', 'Royal Air Force', 'Medicare (United States)', 'Free agent', 'Random-access memory', 'Los Angeles Times', 'United States Soccer Federation', 'Linkin Park', 'Superman', 'Dream Theater', 'Köppen climate classification', 'Southampton F.C.', 'Intel', 'Conspiracy theory', 'Phoenix, Arizona', 'American Samoa', 'University of California, Los Angeles', 'San Diego', 'A cappella', 'World',
    'FIFA World Cup records and statistics', 'Houston', 'The Twelve Days of Christmas (song)', 'Kendrick Lamar', '2023 AFC Asian Cup', 'A. J. Brown', 'Aerosmith', 'Pixar', 'Function (mathematics)', 'Spider-Man: Into the Spider-Verse', 'Meta Platforms', 'Patent', 'Football pitch', 'The Magic Flute', 'Shin Ultraman', 'AM broadcasting', 'Al Gore', 'Suits (American TV series)', 'Work (physics)', 'Cleveland', 'Boeing 777', 'Reading', 'Giannis Antetokounmpo', 'The Elf on the Shelf', 'Value-added tax', 'Oldham Athletic A.F.C.', 'What a Wonderful World', "The Last of Us",
    'Lionel Messi', 'Festivus', 'The Specials', 'The Sound of Music (film)', "Newell's Old Boys", 'Reborn Rich', 'Christopher Plummer', 'Steve Cohen (businessman)', 'Index of Windows games (A)', 'Aliens (film)', 'Helen Mirren', 'S.S.C. Napoli', 'Club Atlético River Plate', 'Boca Juniors', 'Die Hard (film series)', 'A Charlie Brown Christmas', 'Aldous Huxley', 'Imran Khan', 'Pope Benedict XVI', 'To Kill a Mockingbird', 'Pokémon Ultimate Journeys: The Series', 'Siniša Mihajlović', 'Mickey Rooney', 'Characters of the DC Extended Universe', '2023 Africa Cup of Nations', "Catherine O'Hara", 'Richard Harris', 'Paulo Dybala', 'Martin McDonagh', "You're a Mean One, Mr. Grinch", 'John Lithgow', 'FA Trophy', 'White Christmas (song)', 'A Visit from St. Nicholas', 'The Year Without a Santa Claus', 'Joker: Folie à Deux', 'Leo Varadkar', 'Pinocchio', 'A Star Is Born (2018 film)', 'Hamza Yassin', 'A Christmas Carol (2009 film)', 'Warner Bros.', 'Succession to the British throne', 'M. Night Shyamalan', 'Ebenezer Scrooge', 'Ahmedabad', 'Bryan Cranston', 'Pope', 'A. R. Rahman', 'Leandro Paredes', 'Herbert Hoover', 'Debbie Reynolds', 'Julianne Moore', 'Betty White', 'Paolo Maldini', 'Edie Falco', 'Central African Republic', 'Baronet', 'Kiefer Sutherland', 'Microsoft Azure', 'NCAA Division I', 'A Bad Moms Christmas', 'Genus', 'Gerard Way', 'The Muppet Christmas Carol', 'The Dark Knight', 'AJ Styles', 'Frozen (2013 film)', 'Bardo, False Chronicle of a Handful of Truths', 'Prakash Raj', 'Robbie Coltrane', 'Sidney Poitier', 'Chuck Berry', 'Los Angeles Dodgers', 'Oakland Athletics', 'Watford F.C.', 'Skyfall', 'Sheffield United F.C.', 'Glossary of chess', 'Professional wrestling match types', 'Nigella Lawson', 'A Man Called Otto', 'Scrooge (1951 film)',
    'Alexandria Ocasio-Cortez', 'George R. R. Martin', 'Mathematical model', 'Richard Rodgers', "Groucho Marx","December 2022 North American winter storm","Indianapolis","Atal Bihari Vajpayee","Metropolitan statistical area","Alfred North Whitehead","Star Wars: The Force Awakens","John Elway","Buddy Holly","2023 World Junior Ice Hockey Championships","Paul Anka","Grease (film)","E.T. the Extra-Terrestrial","Niagara Falls","Die Hard with a Vengeance","Bette Davis","Forrest Gump","The Home Depot","Thomas Becket","Requiem for a Dream","Martha Stewart","Isaac Asimov","Michelle Williams (actress)","Rupert Grint","Axolotl","Gillian Anderson","Halle Berry","Savannah, Georgia","Variance","The Football Association","Board game","Straw man","Delta Air Lines","Rastafari","Fantastic Beasts (film series)","Bradford City A.F.C.","A Midsummer Night's Dream","Todd Rundgren","Marlo Thomas",
    "Beck","Flower","Jeff Beck","College football national championships in NCAA Division I FBS","President of India","what is gosip","how is water","Charlton Athletic F.C.","Georgia Bulldogs football","SoFi Stadium","Metro-Goldwyn-Mayer","The Raven","Claire Danes","Abbott Elementary","The Walking Dead (season 11)","Kliff Kingsbury","Graham Potter","A Quiet Place","Ronnie Wood","Ultraman (1966 TV series)","Federal Aviation Administration","Han dynasty","Alfred Russel Wallace","Mac operating systems","Pomerania","I Have a Dream","A24","Primetime Emmy Awards","The A.V. Club","Evan Peters","Christina Aguilera","List of EGOT winners","A. C. Bhaktivedanta Swami Prabhupada","Alan Cumming","Phineas and Ferb","Boy George","Belgian Pro League","Jessica Simpson","LL Cool J","Toyota Supra","James Herriot","Lulu (singer)","Academy Award for Best Actor","Compass","Community (TV series)","Miguel A. Núñez Jr.","Australian Broadcasting Corporation","Phoebe Waller-Bridge","The Flash (2014 TV series)",
    "The Last of Us (HBO)", "Panic! at the Disco","Berkshire Hathaway","Burns supper","Stephen A. Smith","Paul Ince","John Abraham","Forest Green Rovers F.C.","Lolita","Cyndi Lauper","Super Bowl LII","Abdel Fattah el-Sisi","Tommy Chong","Rabbit","Parks and Recreation","Academy Award for Best Actress","The Dark Side of the Moon","Saraswati","Sequoyah","Virginia Woolf","Ron Klain","Thandiwe Newton","Canberra","Circumference","List of Game of Thrones characters","Prime number","Alexander Skarsgård","KL Rahul","Rainbow","Alfred the Great","J. Cole","Hexagon","ESPN","Jennifer Garner","Zac Taylor","The Kid Laroi","Carlo Ancelotti","Julia Louis-Dreyfus","Paul Giamatti","Harley-Davidson","Cardiff City F.C.","Death of a Salesman","Los Angeles County, California",
    "Unicode subscripts and superscripts","Enclosed Alphanumerics","Blackboard bold","Fraktur","Ordinal indicator","Enclosed Alphanumeric Supplement","Los Angeles","United States","California","Muhammad Ali","ISBN","U.S. state","Singapore","Bachelor of Arts","Edgar Allan Poe","Saudi Arabia","Hong Kong","Madonna","Chicago","Arnold Schwarzenegger","Artificial intelligence","Abraham Lincoln","Steven Spielberg","George Washington","Taylor Swift","FC Barcelona","Wolfgang Amadeus Mozart","Elvis Presley","United Arab Emirates","Premier League","Manchester City F.C.","Philadelphia","Marvel Cinematic Universe","National Basketball Association","Jennifer Lopez","Martin Luther King Jr.","Marilyn Monroe","Albert Einstein","Lady Gaga","Tupac Shakur","Atlanta","John F. Kennedy","George VI","List of United States representatives from New York","Dubai","Egypt","Ilhan Omar","Nancy Pelosi","Cloud computing","Hawaii","German language","Frank Sinatra","Henry Kissinger","A.C. Milan","Cricket","Franklin D. Roosevelt","Ronald Reagan","Spotify", "Cher","Once Upon a Time in Hollywood","Los Angeles Rams","Theodore Roosevelt","Bill Clinton","Anita Baker","Zinedine Zidane","Anne Boleyn","Gene Hackman","Fenerbahçe S.K. (football)","Megan Mullally","Mötley Crüe","Lunch atop a Skyscraper","2026 FIFA World Cup","Harry Connick Jr.","Charles Lindbergh","ISO 216","Jill Biden","Tim Allen","Millet","FIFA","Eddie Howe",
    "Serie A","ASAP Rocky","Katy Perry","Gerald Ford","Jimmy Carter","Alexander Hamilton","Richard Nixon","Star Wars","Black hole","Lil Wayne","WWE","Willie Nelson","HTML","Lyndon B. Johnson","Thomas Jefferson","Naruto","NASA","Volodymyr Zelenskyy","John Adams","Rihanna","Lana Del Rey","Leeds United F.C.","A. J. McCarron","George Orwell","Email client","Olivia Newton-John","50 Cent","Detroit","Chadwick Boseman","Toyota","Andrew Jackson","Woodrow Wilson","The Lord of the Rings","List of sovereign states","Game of Thrones","Los Angeles Lakers","Wicket","Sigmund Freud","Ulysses S. Grant","Dwight D. Eisenhower","Columbia Pictures","Harry S. Truman","Oscar Wilde","A. P. J. Abdul Kalam","Temperature","Attention deficit hyperactivity disorder","Marcus Rashford","Benjamin Franklin","Neil Armstrong","Freddie Mercury","Radiohead","Catherine Zeta-Jones","Freemasonry","Jennifer Lawrence","List of municipalities in Michigan","Bernie Sanders","Year","Ernest Hemingway","FA Cup","Damian Lillard","Atlético Madrid","Tilde","Robin Williams","Ben Affleck","Rabindranath Tagore","ABBA","Christopher Columbus","Solar System","The Big Bang Theory","New Orleans","SZA","Bipolar disorder","Stan Lee","Kate Winslet","Glass Onion: A Knives Out Mystery","Binomial nomenclature","Kevin Bacon","William Shatner","IBM","Anno Domini","Kelsea Ballerini","Eastern Time Zone","Socrates","List of A Song of Ice and Fire characters","Burt Bacharach","Social media","Carrie Fisher","Hayden Panettiere","Lupang Hinirang","Banksy","Rowan Atkinson","Airbus A380","Minnesota","Mobile country code","List of United States counties and county equivalents","Minor League Baseball",
    "Grover Cleveland","Pittsburgh","A-side and B-side","Jewel (singer)","Blade Runner","Alan Turing","India women's national cricket team","Segunda División","Vanessa Hudgens","Juventus F.C.","Thomas Edison","Lamborghini","Adidas","Noam Chomsky","PinkPantheress","Warren G. Harding","RDFa","Gwen Stefani","Campeonato Brasileiro Série A","Lion","Flag of the United States","Sarah Silverman","Longitude","Coffee","The Silence of the Lambs (film)","A Song of Ice and Fire","William McKinley","Andrew Johnson","ISO 4217","John Quincy Adams","William Howard Taft","S.L. Benfica","Rita Ora","Alan Alda","Rugby union","Columbia University","Dallas","Billy Crudup","Geographic coordinate system","Texas A&M University","James Joyce","Encyclopedia","James A. Garfield","Constitution of the United States","Romelu Lukaku","El Camino: A Breaking Bad Movie","Evan Rachel Wood","Ray Kroc","ASEAN","NPR","Tomato","DNA","Real Betis","Eugene Levy","William Henry Harrison","AS Monaco FC",

]

user_id=['CoYPcYYGWC@outlook.com', 'AkQuYCkSaQ@outlook.com', 'SAQkhtvJsP@outlook.com',"YkkjKhTksu@outlook.com","GxvmQLXPzM@outlook.com","TRyYdctPCX@outlook.com",'obkXppCriJ@outlook.com', 'xZKGDZzQiK@outlook.com', 'MBgFjPzCGo@outlook.com','kcbUtKIRve@outlook.com', 'PcZXPBryuc@outlook.com', 'tGHnRUnUiQ@outlook.com',"sxRUlrgeSb@outlook.com","bPiCcdQiIp@outlook.com"]

for n in user_id:
    driver =webdriver.Chrome("C:\\Users\\naren\\Desktop\\New folder\\chromedriver.exe")
    driver.get("https://rewards.bing.com")


    # sign in process
    # i0116
    mail=driver.find_element("id","i0116")
    mail.send_keys(n)
    # idSIButton9
    time.sleep(1)
    next_button=driver.find_element("id","idSIButton9")
    next_button.click()
    time.sleep(5)
    pwd=driver.find_element("id","i0118")
    pwd.send_keys("Idontknow")
    time.sleep(1)

    sign_button=driver.find_element("id","idSIButton9")
    sign_button.click()
    time.sleep(2)


    # stay sign in ki button
    # idBtn_Back
    idBtn_Back= driver.find_element("id","idBtn_Back")
    idBtn_Back.click()
    time.sleep(1)
    driver.get("https://www.bing.com")
    time.sleep(1)

    for i in range(60):
        search=driver.find_element("id","sb_form_q")
        # time.sleep(20)
    
        word=random.choices(words,k=1)
        word="".join(word)
        search.send_keys(word)
        search.send_keys(Keys.RETURN)
        time.sleep(2)


    driver.close()
    print("done.................")


    

    # time.sleep(45)

