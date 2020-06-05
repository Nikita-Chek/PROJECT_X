import inverseByModule as iBM
import sys
import random

euler = lambda p1, p2: (p1-1) * (p2-1)

def encryption(msg, ex, n):
	msg = msg.encode('utf-8')
	msg = int.from_bytes(msg, 'big')
	return str(pow(msg, ex, n)).encode('utf-8')

def decryption(msg, p1, p2):
	msg = int(msg.decode())
	n = p1 * p2
	eul = euler(p1,p2)
	ex = e(eul)
	d = iBM.inverseBM(ex, eul)
	msg = pow(msg, d, n)
	msg = msg.to_bytes((msg.bit_length() + 7) // 8, 'big').decode('utf-8')
	return msg

def e(phi):
	exponents = [17, 257, 65537]
	for _ in exponents:
		if (iBM.gcd(_, phi)[0] == 1) and (_ < phi):
			return _
	return Exception

def key_generate():
	primes = [19273843521026396942423041256702416467190916480829438372892895532230844179797565880221360136918107451198911623615771273474843394785083334295101581743836650077544389834600122094987552690583700099541822627492515524020980656689705115960283286209148940535104015337,
		  	  67456772536997811174562843827334166492604722726798354062809571765666143205478154891520988418820829227136251602140592962830914859588069638333300746582776692720637910854613289610057151587251089921722318897093966945777208101090776716402383331743368026418397556891,
		  	  42593488731436334558240129827571664214680272396207168234413236480365708090391898200141852152164946968094921114819348676422927981034847486684273805683705118394194048620602183332746250604729056069042068601678865748440018982946827563704509942977277090795264187849,
		  	  16107407153096872818493782945957787561325375534122812732915532201840816254400467958193423121840372946330339589450123508622134774121104116098949168616561321246035895208358144099325905467103390396346965217633409955370491728893923457194644438929148135544797769069,
		  	  49642196519287563890219771644794994818956271978536893649678493707106697740616207443433039867021200759433868948129547546653564382798817640018032929084872815787149827529492755939735263141371178259217768571082104248486704273772193856448675375667327678108529811271,
		  	  10630035406473276537672417642319966571896173296326470196334200433213809269253309428418308671153351545251256200022353395036694442206579095070868233809133290885233924975320623561025978127184373556464786419456515838125085169778530098251536033042380621776798416689,
		  	  25290181317443223202462289639535568588026980307751030325846138922434211534444969788237980189518561067454419530259429589051181436567403701018238964718203056168955426581729913704293743890489851209326371108494646496297959925452431230546049667449322574935832180327,
		  	  60960130920852832345025772583794322476182120995079063265343175376976500914414814270586102634219293014759814314143899859216943973261216488178461281369867855351998227521639452187585065453508673607852739488682524197867887816471871859348497859187835981791349272159,
		  	  58647870561379694776505017720198012685284549950782634875879337136907456988455829016630334078898426016854099512329679724649329704688926137344357301398956973920710342405083924140345133464332875812901929569113000763985040682896337370547264220717137594746886327761,
		  	  50985706168761488366316382338014644105350894561341788683522249832194333902444754897729974158787863583439645933374661244079621367847162487366917832904994676462834272619451739021241059378594481762281376106663491397418420352316354537398792605354478235631207230857]
	p1 = random.choice(primes)
	p2 = random.choice(primes)
	n = p1 * p2
	ex = e(euler(p1, p2))
	t1 = (p1,p2)
	t2 = (ex,n)
	return (t1, t2)


# k = key_generate()
# f = encryption('huid', k[1][0], k[1][1])
# print(sys.getsizeof(f))
# print(f)

# f = decryption(f, k[0][0], k[0][1])
# print(f)