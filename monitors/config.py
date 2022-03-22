POSTGRES_USER_NAME = ''
POSTGRES_DB_NAME = ''
POSTGRES_DB_PORT = ''
POSTGRES_DB_HOST = ''
POSTGRES_DB_PASSWORD = ''

WIN_PERCENT = 0.05
PRIZE_POOL_ADDRESS = 'osmo1lyz7awgu2q3hjd0uwsuys9jg2gqalqlky0xa4p'

NETWORKS = [
    ('http://136.243.176.155:1317', 'osmovaloper13tk45jkxgf7w0nxquup3suwaz2tx483xe832ge', 'osmosis', 'uosmo'),
    ('https://lcd.bostrom.cybernode.ai', 'bostromvaloper1ydc5fy9fjdygvgw36u49yj39fr67pd9m5qexm8', 'bostrom', 'boot'),
    ('http://88.99.253.239:1317', 'junovaloper1quqxfrxkycr0uzt4yk0d57tcq3zk7srm7sm6r8', 'juno', 'ujuno'),
    ('http://65.21.153.48:1317', 'emoneyvaloper149vyxd36kxpg46rralaw6eejv4d9daqc3nv642', 'emoney', 'ungm'),
    ('http://144.76.94.124:36317', 'microvaloper13mkjrr578sxd7whex3mqru96vdt3tttw63uwtd', 'microtick', 'utick'),
    ('http://195.201.161.56:1317', 'starsvaloper1y58hfnm90r4efhlydx0gavz57lvm7k6uulkg3h', 'stargaze', 'ustars'),
    ('http://88.99.218.28:1317', 'gravityvaloper1vyd4k5j636erx5y5kdqghdu3rfjtwc48vdc7r6', 'gravity-bridge', 'ugraviton')
]

BLACK_LIST = [
    'osmo14nzyt8wmx4g6zkeluelukamgsh5v4xgnnzn4j8',
    'osmo1cg79pj70mgl8xlum0rw5yy6enk9jszsrfyf8cx',
    'osmo1tqdvlku97p88z5ndf3jz55vnccmzgs8jla375r',
    'osmo1s2a7rckcky6jmhncxwy0xtwf2ymg87puaj4z2h',
    'osmo1pvxhtre74l37p6y2rs2e8xyek75z7xlc7g2trt',
    'emoney1cpfn66xumevrx755m4qxgezw9j5s86qkan5ch8',
    'stars139a4n6w6dhwv60dj2clgwm6r0q84gju28z9at0',
    'stars15gp36gk6jvfupy8rc4segppa38lhm3helm5f8k',
    'stars168efxgnh55vcgx83x90pw2fves9anw8kmnlsf5',
    'stars1pu39c2nc6k6mc5yvp5qqpfccc5lxpghccx7ggl',
    'stars1dpzvwefvm56scev2jpayk2xvjwg3r4yjpfrsxv',
    'stars1pyap57v77g55d4yz3yynkynfuju02x087cavnp',
    'osmo1gmc3y8scyx9nemnuk8tj0678mn4w5l78343qvh',
    'osmo13tk45jkxgf7w0nxquup3suwaz2tx483xrsefl7',
    'juno1quqxfrxkycr0uzt4yk0d57tcq3zk7srmpdd4c7',
    'micro13mkjrr578sxd7whex3mqru96vdt3tttwet6cq2',
    'emoney149vyxd36kxpg46rralaw6eejv4d9daqckn2wt8',
    'bostrom1ydc5fy9fjdygvgw36u49yj39fr67pd9mv67ety',
    'stars1y58hfnm90r4efhlydx0gavz57lvm7k6uhpzu20',
    'juno190g5j8aszqhvtg7cprmev8xcxs6csra7xnk3n3',
    'gravity1xyqtlquzgtumv496rvjnh6543daa7mkpkvjwd4',
    'juno1aeh8gqu9wr4u8ev6edlgfq03rcy6v5twfn0ja8',
    'bostrom1g07gj9ph0r2hjx6ffqn8vl38u4agd5mpqx9m7f',
    'bostrom1pntx8ql2v7cqxu05etg8c4v0r2vz7qnq9uqmpy',
    'bostrom1gxhs5wzam5rlgf6cs0lkme400ut64d4ncpfs2h',
    'bostrom1tr3eyy9l480pxjk0ygudwpfus7j8pgdljn09jm',
    'bostrom1ttd4h585vgy29gj0xe0p338drvw9w4m4hzwj9p',
    'bostrom1t3222ju7ssu58xsm3m2xw445p94cqn2qrex3vy',
    'bostrom1w4tvyvf3hhpcwv9d4axa8n0mmj5d6ypvpq5mj6',
    'bostrom1s4wntr9selfaznc2ezjkwnwt2y0terx9tqpda3',
    'bostrom1smtmk8fe3qhlwj3h7nynl6p42946qydzvgj9va',
    'bostrom17a7xxqa4drnalvv7pkxrkxqer953fdke3ulwx4',
    'bostrom1lvkzyfaqjn87cfl65a55nuqt8u6uhnyuvhp8kr',
    'gravity13l0z8wcsak6z04xvn0m3ayacvp5ngde2ffgjyv',
    'gravity1heyxccc9z7at2hj9ecuygdy5cws9ty99853u7e',
    'stars1zc0xspsrjv24krgmslxza4zqmtva4qjnr0j0j2',
    'stars1xuvqqtpav938pskxzslwv6x9xvs3yg456ud32f',
    'stars18vf0hrxedgj9v8zf4pengmz4d4c3gzngkx5k9z',
    'stars1jmvdlyau9h52arp6s6836k7m8u6xkuf7qgz32f',
    'stars17a0xkhvnavt3fx5rfkrq89gkt0genewqjng0wv',
]

TOKENS = {
    "uosmo": "uosmo",
    "ibc/1DC495FCEFDA068A3820F903EDBD78B942FBD204D7E93D3BA2B432E9669D1A59": "ungm",
    "ibc/FE2CD1E6828EC0FAB8AF39BAC45BC25B965BA67CCBC50C13A14BD610B0D1E2C4": "boot",
    "ibc/987C17B11ABC2B20019178ACE62929FE9840202CE79498E29FE8E5CB02B7C0A4": "ustars",
    "ibc/46B44899322F3CD854D2D46DEEF881958467CDD4B3B10086DA49296BBED94BED": "ujuno",
    "ibc/655BCEF3CDEBE32863FF281DBBE3B06160339E9897DC9C9C9821932A5F8BA6F8": "utick",
    "ibc/E97634A40119F1898989C2A23224ED83FDD0A57EA46B3A094E287288D1672B44": "ugraviton"
}
