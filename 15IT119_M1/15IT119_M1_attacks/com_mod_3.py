import sys
sys.setrecursionlimit(1000000)


def ex_euc_alg(e1,e2):
	if e1==0:
		return (e2,0,1)
	else:
		g,x,y=ex_euc_alg(e2%e1,e1)
		return (g,y-(e2//e1)*x,x)

def invert(a,n):
	return a+n


c1 = 4241390948746024180732987587331318923870614972291777497392007343918055652231369959871105248610486372799946888568993379572060829358573904113167238030245537751361766369031746955250889485226280737787501735370197014550499207039725256134325268092258291429674808682749972531553213389249121689702088913917147
c2 = 4644981130851613214916555838987623677938404507393978370609572978681882690643865828025417518616757463435205326863172547049499846026186425340262963892569726052382319949708809694364360001788000779266842357836576944128839463335376334629460256818830396904702767792027283973592332680418031195718028960744261

n = 8198490354395201951358627804442014577276951511370975986950461043103618994243563652354156980958689724400543430260620045425969303650427386412905712197692655458626052138749400882601179489151925419998301565237964612090705052214772232752828273157156430155823399581708492748844286854408210547193011538602733
e1 = 2755482985513679438161591925053332795438753935726058140228739732433094016312049474173040384983794334581180823438809528965489430549117798255660021980197543923631705038010897695205498787407479838661927624508417954673327724013682996699408123273338279027646713318131507185835472865631348078796749652499613
e2 = 6331776772639025560368118516199409640901383563893321959098950657289012938389433282589183086122947565512248094064082840746314967708921693143717963512628697372066645334250252603168921773058961416551682269082369047218392764296970695592696765975505985783316105123188145417657753206518784984424762249962997

print "C1 is %d \n C2 is %d \n N is %d \n E1 is %d \n E2 is %d" % (c1,c2,n,e1,e2)

g,x,y=ex_euc_alg(e1,e2)
if(g==1):
	if(x<0):
		x=invert(x,n)
	if(y<0):
		y=invert(y,n)
	c1x=pow(c1,x,n)
	c2y=pow(c2,y,n)
	m1=c1x*c2y
	m=m1 % n
print "\nThe decoded message is %d" %m
