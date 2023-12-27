from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nrows = len(heights)
        ncols = len(heights[0])

        efforts = [[None for j in range(ncols)] for i in range(nrows)]

        efforts[0][0] = 0
        tovisit = [(0,0)]

        def processNextVisit(visit, nextVisit):
            #print("visit", visit, "nextVisit", nextVisit)
            diff = abs(heights[visit[0]][visit[1]] - heights[nextVisit[0]][nextVisit[1]])
            effort = max(diff, efforts[visit[0]][visit[1]])
            #print("diff", diff, "effort", effort)
            if efforts[nextVisit[0]][nextVisit[1]] is None or effort < efforts[nextVisit[0]][nextVisit[1]]:
                efforts[nextVisit[0]][nextVisit[1]] = effort
                if nextVisit[0] != nrows-1 or nextVisit[1] != ncols-1:
                    tovisit.append(nextVisit)
                if efforts[nrows-1][ncols-1] and efforts[nextVisit[0]][nextVisit[1]] > efforts[nrows-1][ncols-1]:
                    return False

            return True

        while tovisit:
            #print(tovisit)
            visit = tovisit.pop()
            #print(efforts)

            #UP
            if visit[0] - 1 >= 0:
                nextVisit = (visit[0]-1, visit[1])
                if not processNextVisit(visit, nextVisit):
                    continue

            #DOWN
            if visit[0] + 1 < nrows:
                nextVisit = (visit[0]+1, visit[1])
                if not processNextVisit(visit, nextVisit):
                    continue

            #LEFT
            if visit[1] - 1 >= 0:
                nextVisit = (visit[0], visit[1]-1)
                if not processNextVisit(visit, nextVisit):
                    continue

            #RIGHT
            if visit[1] + 1 < ncols:
                nextVisit = (visit[0], visit[1]+1)
                if not processNextVisit(visit, nextVisit):
                    continue

        return efforts[nrows-1][ncols-1]


s = Solution()
print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(s.minimumEffortPath( [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
print(s.minimumEffortPath( [[143791,99629,279476,535618,301267,615502,801736,135969,873268,739077,138400,685720,188963,651266,785178,883955,315149,560815,197663,819794,8803,474618,664851,136935,542960,103626,718947,173382,375703,808864,32469,223243,995391,735217,23026,133552,235094,501538,876182,15192],[244226,742715,459211,827349,910036,176491,296383,656123,819222,42672,800067,404231,108800,904912,768262,978726,967075,773897,27670,495793,500201,143186,991506,990945,73014,234522,330891,10025,341704,795367,375247,718762,40570,85185,993752,440055,137727,540182,760171,765509],[188935,132549,481309,213934,345157,129551,821539,706260,865295,992739,998795,231324,887242,176495,455477,598474,921842,930805,48908,608095,319598,633559,304376,737064,47139,696219,840513,16978,502592,620248,700491,18389,965439,283375,518323,924010,443967,871418,781815,123798],[91010,772224,395418,332817,781774,525305,410880,275150,488214,421455,525823,843513,559467,158179,366233,446329,415758,382290,189292,102436,797257,108231,738127,427522,227901,961800,526726,271665,328880,424196,670516,854264,880969,271361,671796,923890,616512,381555,930887,340444],[517732,226514,141554,520082,497705,729033,483101,134137,861883,553984,366206,73797,133598,322324,546750,254946,430225,558450,1087,635341,93229,698160,144603,586310,53079,723665,581864,311199,26570,325967,35492,827850,885629,593986,10070,111374,878244,999274,167604,329159],[410717,927405,71452,532049,828098,890303,736250,605786,260982,311893,891209,713109,264638,314354,399923,696333,873349,563223,691408,399215,305646,436604,62016,724043,301722,817322,292055,56446,116054,652991,621785,734582,985608,615901,888003,832483,365690,637978,596031,308286],[619886,102023,519271,449598,4633,396045,550214,378583,297025,694960,999130,409386,547818,484565,149633,769148,199867,170510,650387,965675,457889,836459,612600,366473,509343,354777,428705,742275,181747,564018,369582,45467,111821,31078,262649,354919,6379,526120,830874,353908],[827200,804313,180918,364132,580718,733231,600110,518967,456307,568477,743916,656424,935839,798707,684440,401080,701966,144278,389993,918965,362894,306066,86551,165593,887669,112899,983614,620951,189766,894790,138416,395691,906684,218441,904875,579348,48418,745601,101171,642702],[221471,510800,763292,870353,71490,237133,737453,501711,527608,342602,140534,746539,612778,58909,465834,877336,58528,779495,831709,442851,695222,560998,69683,190582,112447,413668,231726,797087,279301,912905,233839,649374,54917,729054,352614,983228,615497,946237,182932,109],[457728,697990,949625,633029,526737,969266,352881,948774,870420,715562,20770,494752,891905,50069,315374,512764,194575,1422,143624,722255,670009,438788,631423,904211,719934,996016,203617,404184,118774,771835,216978,612910,20182,892087,6563,981636,975518,805493,390796,493825],[626672,260901,400203,918202,372935,412925,738393,289456,626571,109040,141271,453434,422263,825276,453423,987231,125715,699685,780362,218735,960259,748469,338068,967203,34219,428796,127648,895259,448180,693938,815330,350505,876930,51527,843543,109570,138526,296251,368951,223458],[843376,187493,123432,511744,932342,559348,823595,278059,179862,288107,521267,449264,25462,967234,328541,255506,207801,486512,721789,557818,657453,431961,262152,596281,931982,337902,476085,295785,445686,128885,237205,224705,942835,567828,503816,291305,775603,70351,13952,477734],[6016,12032,319330,561546,357473,310856,160629,434041,573191,295559,913295,872944,47526,216436,467045,93051,606899,851292,948917,1449,248036,691582,61186,405075,538145,290221,619463,238672,46654,194316,512084,449932,608981,268538,323080,44084,55063,677995,477107,686954],[630721,801386,30334,778362,962242,799225,465279,216034,230683,204348,664952,646933,718199,883580,568542,580796,511721,645056,103121,469547,773498,152991,125031,653469,524345,57136,916950,43309,620413,117740,999058,941406,545039,845310,126246,18706,887257,224203,49228,926390],[910052,292330,738405,633176,971371,807773,572992,856306,849034,922979,914963,670929,761519,620633,8211,288130,214197,906273,671404,452637,981817,127551,650915,518559,157590,410363,635772,683898,584956,5514,511235,40364,436218,862954,83400,512047,219645,800596,970752,266842],[506784,856289,172522,735453,346375,882833,307049,414681,756853,284212,235030,720496,20727,818041,707,101245,877089,150558,31506,440970,398333,118032,512000,294065,211204,123724,178433,445227,652624,41542,632654,789624,629242,611697,396780,662775,172246,227420,431831,985544],[479660,637090,281933,424085,339188,793981,204897,489017,147813,355368,973801,513581,722807,59565,538545,475876,43485,836507,4349,954254,841679,405367,224725,526477,531075,719930,823666,214443,931730,347324,929889,735706,609585,402374,420250,895407,427764,151522,326118,636135],[430476,299363,990722,792817,892520,505204,321007,401029,766665,731480,173370,553507,643289,704514,372565,455286,163347,212293,620000,954353,573371,235907,340988,209502,715283,742676,942096,573104,164976,101326,63975,216210,808504,456613,190857,107420,610797,208971,987595,214295],[128292,774590,429933,263203,502515,402404,695308,697051,95832,919401,990613,769394,109462,578537,85070,382662,280435,231944,782763,579410,473383,890926,93290,952200,965451,136867,797809,626621,734442,806804,386717,267534,137242,204740,574213,966795,222283,885029,299802,994957],[263182,194245,417543,789042,144465,146955,919478,705386,846907,68242,676221,228132,177966,619271,683218,33372,587534,752421,963488,331841,809202,601047,199602,927156,838656,980883,327484,420238,263104,643026,390674,947242,253181,16315,721396,506309,18739,382499,266402,514411],[917245,883759,158981,306940,959974,231537,569634,651810,989362,251439,760233,368513,710192,619829,36364,547940,65058,853421,701026,50192,879592,319295,247543,824003,997713,34330,731583,227164,915648,750327,826371,280584,601910,349455,445403,613835,876288,987305,154722,309725],[71850,941610,420711,816750,632416,58534,29817,118275,135849,69318,810869,821051,985797,730910,300520,859360,813658,699113,804067,572134,652882,700706,513259,956697,496863,429418,144807,115943,930390,415523,308878,912265,221612,142013,146568,901804,966915,407943,728746,638522],[662628,357161,398962,357940,668335,675644,877869,287583,818184,490164,940488,770075,791367,510222,938140,233559,272022,428654,528600,195129,632060,81813,775569,87338,115887,875165,683627,592830,890462,615747,554533,150723,846651,803567,412225,849111,617879,493678,390061,73261],[377382,28221,226699,153364,854507,453675,47485,757229,77393,777954,882050,5019,17482,339149,393666,942674,578328,224793,938510,88822,859976,665508,85027,213444,366096,404237,842050,123093,980133,684581,910745,725102,235234,529812,404741,177294,455510,960247,334296,829633],[867026,521862,73989,538566,253189,931088,187669,458595,592379,437485,127142,286837,932199,213453,211616,516291,911132,222511,200868,45528,616322,953333,326048,415455,838046,259664,862297,81480,542120,947526,962570,714065,171995,175100,766277,314174,648544,42644,494732,690433],[234467,309173,428951,764716,549997,71969,633955,107463,945768,267494,662640,957233,250747,302667,252471,255565,762896,58743,988549,175888,649760,365048,116381,739428,332189,626743,186111,774914,841903,41920,850842,697661,355253,455971,953829,31605,982354,562839,998087,175763],[283681,893329,315843,341025,957392,29516,918073,14688,841603,309777,452163,655847,694883,401476,721025,811567,103974,148511,253601,242466,644788,925875,768068,567442,12842,393542,203165,860985,224810,415583,291712,555906,786556,505724,389680,622146,933264,106960,22110,404370],[590154,610009,906913,940178,125182,208893,57270,875399,69737,163154,638051,522912,796654,361507,645872,751174,620595,682140,913501,37859,400158,482014,414024,569784,85070,397347,192813,237251,501967,356559,497458,743401,129953,369170,934690,126271,657227,143036,547488,77488],[318284,957729,131195,638112,598464,761477,983658,974366,157186,364709,66379,895851,720909,455064,166891,975419,702911,719096,144185,838735,555354,252108,532885,864137,305320,384616,506086,664128,948524,901096,677891,572023,339909,795817,459552,621763,999870,526935,115190,763156],[571241,98949,218923,82144,715070,597192,744416,241053,990420,763555,182896,284661,3852,600482,288966,362049,885498,680718,646424,507135,328667,170477,527807,978347,227909,422712,668970,286226,668383,965132,947918,3696,808161,989242,473549,966312,610401,946123,66365,831110],[591221,460670,912568,443383,906319,49625,269438,574587,422608,418668,886237,812101,487015,210272,496554,236417,797480,450452,760587,573100,857665,529951,797653,777792,74202,550132,234335,604156,371462,517495,38865,830296,537829,452369,317740,669817,634022,452042,223567,785071],[552600,161708,839549,197531,259615,541999,190227,913803,539003,584459,589129,887078,183839,141944,445722,665996,955374,633086,447614,742124,130751,795828,621482,834988,858744,201576,856275,806226,945136,35066,487283,766618,416075,754984,406503,488761,790602,534024,422755,767139],[619680,710341,626113,319373,115717,466611,68931,260424,251225,28791,194442,654006,784211,580946,809345,643758,849402,817695,81082,104156,295040,71406,330470,626521,964025,156513,27605,388258,740489,430837,680548,600050,593153,364704,845482,100809,450476,696437,293382,352496],[585109,734496,711182,39579,360584,342667,160045,634029,968583,673986,125743,41650,346513,249028,138501,906437,555455,621860,437955,409447,56119,632288,676155,176860,590012,660703,713975,981535,183663,156440,82666,102766,873376,332503,27197,306641,859311,642137,800751,663551],[12078,161122,639803,664066,114463,922999,949689,708183,100450,185475,755414,731636,219948,948323,971460,994792,336389,977869,375526,699480,918466,198569,935974,404578,276038,871046,919199,265505,987745,977492,533497,899000,482975,118042,607804,744596,582423,518795,300844,613896],[217173,277671,904934,325323,174962,459930,836280,192266,227390,654124,96569,594516,155246,354703,475873,348328,363699,453169,372676,870398,443894,937141,380299,689284,823641,775513,999220,439816,623632,662657,701995,803908,377827,43061,815822,928528,968901,87736,795924,990040],[758567,831776,660998,563469,179712,212717,532950,572929,320779,281068,575605,690374,97897,996438,191523,456617,697221,621247,150262,787877,420511,905967,168272,73659,885597,370316,399623,548393,621916,953080,703938,592420,131920,106392,746222,997681,208186,996321,772459,976224],[554976,303632,604667,821288,119027,491692,750482,853619,5534,994249,401190,189055,561698,364597,14389,708770,414484,880823,316585,797089,793203,730986,638910,85701,128952,558771,297931,360110,99103,752049,506700,373096,265829,50424,974851,680666,790361,779451,654014,147167],[240122,840135,296146,687075,434548,748188,763702,616453,884633,247204,578042,68643,214468,945459,855869,498325,349341,566628,165843,432527,95750,670060,953994,252933,613885,558457,830318,59185,355677,284310,431036,113308,928321,157211,935727,963583,600149,607190,560021,592001],[754048,289782,196577,607605,146726,158771,839795,339395,272709,402960,535701,81102,418988,959442,994004,846449,702891,863832,852045,853439,162850,620684,834343,186720,414065,683801,53556,338520,878113,639215,384143,749040,132990,850352,904948,289385,914373,625761,970293,307471],[169352,565849,996596,829283,535175,519474,886664,385058,783628,594302,649694,215243,820565,151140,460419,232364,814106,465317,523202,182276,127851,531073,928770,448967,657622,928026,700648,770406,721259,444268,28426,902492,377189,472751,795137,581684,775527,540582,63232,541537],[17405,108183,340750,891262,275591,470660,213898,676315,883497,238175,928055,487843,659901,547733,307672,605525,978634,305818,303528,354153,707817,430686,666798,115774,215294,685322,681920,301652,369239,721522,865181,749709,29467,219369,424319,64667,822243,443969,682547,119465],[953694,997022,61559,910793,533939,377201,898969,566969,6109,810692,344145,999025,91761,153696,408920,408471,800560,846741,695463,304611,445483,960749,120750,404415,220303,795645,228251,532999,346458,170984,821460,949603,490385,868637,672667,644990,321101,252588,258715,778508],[647006,103336,188861,139304,891396,225287,250960,528162,345101,742150,850765,450876,719111,613045,274935,183828,487192,77680,659166,781360,111459,928165,954574,445586,540787,969255,132994,937976,150778,403550,48833,263680,7842,809502,978404,251948,499555,86385,131387,775713],[280106,782292,261369,936089,653363,656360,707568,624535,3691,911415,47098,338645,510747,678475,226761,249528,562441,613847,955302,15161,791894,258712,757690,19941,651359,239105,789969,893650,861439,232599,45652,311155,35417,935891,276758,704390,883602,570207,603920,603525],[585449,991844,734699,95998,147948,133492,771870,791759,103520,939782,224970,85582,425739,796254,990233,227057,814603,895456,777202,186083,14442,289917,192129,666593,190543,414953,435459,153546,746583,473554,880622,711717,382179,406141,809453,795540,470875,556767,67566,902601],[38063,144619,369231,165473,778883,731118,17266,767513,206628,878010,421490,897936,894064,697270,994336,795709,385833,610473,412520,429148,205921,231878,696793,63348,499460,615865,533057,303985,407298,676963,782397,404746,586328,770402,644884,112798,454171,904038,386087,800474],[318740,936296,195138,455949,569242,588819,90581,625723,396929,726160,30796,751590,209166,887221,206368,216356,358267,997081,755310,766267,10124,19681,117895,12251,616389,979341,171489,614087,150486,241045,87951,789132,509493,377131,529074,216671,313471,18108,863714,263096],[514575,202827,254359,486073,143472,119026,950585,307416,998989,351452,87166,700112,385546,337574,993262,387303,973612,176237,103874,783508,743144,968359,285392,529071,237948,522079,958700,784355,730164,425041,805318,379815,94684,36988,921202,736287,272351,967640,575341,278084],[160000,178009,772056,726530,258148,464477,834022,32421,70192,967463,215803,397824,922850,467085,298430,107481,907288,359782,75426,951965,673234,578639,262644,288768,478316,184491,674772,119616,722929,396495,355491,978541,874470,721920,163430,630010,33608,242683,72713,452117],[918330,417545,777570,414101,818348,917829,221951,336201,926910,837360,437495,700879,233673,471229,51911,911731,866431,826370,744657,993998,566816,383265,358845,823922,660249,367595,418122,267219,524467,78134,676897,3874,724274,873108,779441,105929,463539,498139,816701,592166],[244921,590647,520369,594382,967950,621218,827089,410500,429405,420909,665681,553793,703526,321155,126745,7020,515212,795287,14969,58861,742432,169510,620470,78743,782747,541982,348015,919916,716415,957171,377304,608886,361500,357587,595418,473602,938896,764401,163703,374861],[53426,696402,118909,260188,684319,574656,982310,425525,747649,270293,986136,271704,7155,724228,585847,805923,873321,620748,184243,794325,951786,853101,654113,88263,23006,652214,859315,829623,333361,858272,361379,196617,429007,662576,187865,252983,508353,686861,86369,117634],[603019,484583,66758,604658,793539,87707,29407,551115,375063,539997,87050,669874,30177,324714,700201,962239,785404,36558,6923,810575,956995,725028,582506,115730,535130,994357,640220,168448,856423,801300,640388,137337,565677,29651,234571,61374,473551,335498,995003,537347],[516280,449680,64140,807581,819050,399906,41782,306661,705710,516187,798185,444438,783974,198451,744125,524835,232580,744717,451445,285976,980337,152867,578074,905775,1049,43387,335188,855887,476510,814508,158403,529099,484503,731692,406654,692136,824077,458057,503470,468438],[363088,243437,784743,857718,287233,69797,916273,66244,718311,692312,130519,594065,313651,223273,270631,843897,259435,815589,61084,631714,398256,27808,312915,819260,980248,712094,858686,982268,338788,446970,303073,78464,710075,67099,748162,406093,595010,121699,478042,434018],[114707,810258,678006,700257,329061,597302,322343,712776,335969,645879,127667,465502,314265,764148,276024,259661,845649,722395,472673,461841,859030,902549,558031,766750,58862,890970,483181,430165,374642,221297,410415,985503,478431,989940,469515,132039,940662,301229,5844,631956],[281861,702671,799397,836825,471053,785933,661372,914763,801073,261922,808281,524748,503093,700846,477093,681475,341596,917683,401468,724707,798691,624026,789505,456149,806701,864389,818660,323665,646272,900017,710104,348312,489995,671154,151778,782520,177513,785845,317031,254840],[337790,865831,163070,900593,498045,288676,282909,181617,255323,786738,547939,668015,903219,335138,758631,157424,185638,192586,269383,209042,238625,676978,366355,58572,887518,843161,569676,590930,262944,39621,438863,15156,753875,466583,942665,424868,52876,939440,2192,708785],[453688,523816,490711,21271,769110,569659,679657,596256,165995,571187,875340,41742,985583,517231,629195,376053,592135,30919,94257,182072,557240,946955,820249,843083,635646,664375,473939,949972,735235,650773,795868,973350,295851,588853,881672,587172,437053,638843,798493,630881],[837979,52858,376593,659839,75266,926274,427366,994866,742071,765399,808844,699481,897901,387506,595711,608263,998540,569917,726524,777316,63088,923270,485300,742256,194655,479216,317208,94825,629829,636671,596541,324536,549130,516542,786077,842674,714504,72668,592932,655601],[166002,20750,240317,827081,650512,42512,980134,827665,474880,584712,107816,505248,537827,178973,223632,569277,303738,99967,377869,313815,764421,168016,798072,392169,147328,849237,318967,489562,407468,936265,307360,24135,281894,795692,138462,808785,333274,141131,663956,44945],[221403,767376,969062,930310,518353,390556,692097,338739,346700,605337,499195,554763,416070,571231,761655,923167,389825,392300,393670,919157,1151,488169,318871,624280,94033,662835,660855,461449,152410,940375,838695,679380,443352,994976,289787,963649,620404,335300,562367,941658],[441016,821433,764863,624204,80528,641320,420327,769419,923469,291520,481378,965771,503718,345204,498126,332263,661087,234947,376319,503703,919412,263583,884470,83431,48868,817943,566000,909799,308951,741563,32964,948672,885306,199364,952297,660854,755819,963767,665761,657828],[469040,692343,155843,799433,730728,471877,253144,427068,68427,870757,347339,340851,440045,737303,448878,844690,554688,272024,321033,386895,54278,377896,853553,491487,974799,221490,457603,732605,117451,768793,797239,902777,86300,511812,667,123422,702180,307846,89792,309104],[690384,66665,408770,693125,709478,730005,842691,39581,677431,868118,967520,451620,588039,517101,253775,96521,821724,50242,700705,919155,168160,244896,467373,802117,318299,492908,678609,606278,762683,890457,998059,869592,916428,515037,357395,643262,299116,936581,759975,823783],[995030,302167,211776,332977,550647,947488,70719,382687,509583,718191,989642,577375,58008,581507,42411,348324,178260,176462,585893,833678,465545,929186,252535,914574,339980,661364,634981,137600,995454,132557,174230,428824,893070,636088,811564,706792,734045,771243,800006,106582],[651966,505037,793933,450326,265622,749150,382210,708360,31136,266251,159550,799389,885391,347063,366150,978378,530582,148058,338741,949108,141485,971659,826923,976435,73451,59609,318024,763029,621297,295897,458562,534997,963078,875780,968044,603786,951182,736471,133758,532421],[560569,551169,167275,89384,124807,974003,556425,560445,525885,138648,867698,453821,477548,183066,556832,633693,74472,398604,271144,117852,686391,42794,660592,922785,846288,996410,985431,942537,705389,398816,775448,613656,856653,27814,751213,604529,558534,303129,453570,145533],[321289,954466,811757,368688,13025,626325,113843,295239,687422,694251,854551,606034,162559,999543,416429,536836,620195,105315,764571,847371,160508,63302,949221,474655,482650,497319,499050,469936,253717,596820,454271,957301,638836,58910,961651,386916,571369,266227,475565,117355],[262962,272224,667184,295766,805304,585643,831553,687984,817090,520929,285905,529791,140935,425905,896478,236135,579611,596763,881536,355956,672671,829019,768899,113066,639699,295504,795643,359199,538753,779818,131573,546121,896108,59258,741083,831205,958677,369627,670810,430231],[913386,663621,900267,163148,942106,646076,823444,663966,153214,562975,788349,328600,147464,83573,807006,650096,326232,486605,693346,571765,609433,889366,618812,290355,585143,161217,843934,884251,25992,519178,449623,582827,992397,189728,203947,626667,959724,821562,980578,872256],[995068,839687,140802,332295,270491,628571,423738,177077,135751,884106,443619,511990,4895,102714,190934,213674,42883,915226,50380,523361,694802,219973,87907,182531,590004,646102,422151,440930,319255,745624,60536,936955,70026,922042,797353,265142,323821,270842,698430,75070],[947297,361015,929150,896770,689813,568280,639933,732599,57901,608840,396904,613148,152868,557706,567833,17210,450040,457936,159611,992875,716773,524950,763246,130871,222465,750696,862985,299080,756890,404928,778077,294653,446950,957449,949792,93358,15958,422592,69755,431744],[27116,628801,244219,403400,527063,11516,725827,264252,774041,222702,247500,242551,90496,202231,778806,486341,139575,56495,640757,835839,52892,551073,216219,620376,156186,306915,855588,621378,67831,109962,730941,267756,439307,48789,10689,319748,463031,961315,196138,505227],[630033,279921,499845,834617,474691,85951,257770,214397,460712,678226,13230,296046,28336,801713,30346,597743,277486,271740,396586,968472,330268,866877,565379,339176,761703,735073,126648,448786,394589,752014,860348,2289,564779,782995,858337,263034,58143,146912,121488,622775],[983464,574947,779880,478902,360170,363140,651445,512981,337343,407756,380661,879612,330086,358656,34280,902995,958279,308947,754237,679142,107069,335989,494919,556884,473408,513325,949943,949749,450907,890275,113031,107787,208380,517395,583880,50726,363249,51804,761821,240708],[233999,768282,459785,980581,84740,230593,836598,359007,551295,274442,43885,28141,625340,616534,235713,409107,273045,300217,57999,662165,427996,407712,398570,814359,812969,176792,475053,625005,88506,525476,794805,757240,590986,887232,943223,718300,793982,109585,611433,393810],[198801,947075,771482,145937,877116,462136,279927,210990,795662,94202,423635,89747,599272,235444,496993,636311,79654,387429,144424,529674,310816,253777,17432,464461,768256,372894,731667,515932,713509,140780,456605,280030,162932,629867,862646,334301,883782,282256,350576,918124],[669755,719367,197285,268708,764475,508666,685645,999380,775473,700404,422760,125725,912503,92857,866715,8741,301650,87128,791099,902053,627636,990667,386296,36364,464923,160966,366034,126491,791213,257232,713065,892278,882123,90857,178747,740809,846009,851407,163119,710689],[202214,67075,550610,516481,442368,849737,686000,2449,134993,463512,315434,311895,71944,392877,600298,853946,954507,440554,247990,86107,158192,902720,344086,618968,170973,268381,127689,573677,341017,810726,345395,167516,62397,468621,23329,298157,289144,800177,298085,256670],[433637,370449,269874,273966,760235,46830,274910,906836,259076,450815,760485,822325,70932,217953,424358,44952,628392,145969,962907,468077,243714,904113,937321,858880,943967,33493,414122,217598,373424,451671,842236,665514,426026,870081,831844,777544,449298,419935,974709,421193],[516864,912383,737279,375772,586425,328874,37065,618622,197276,597938,950336,117593,540523,149389,517941,956021,38941,42873,552096,930958,909605,868259,490559,135886,226220,460381,398952,602699,886863,171759,471725,315464,299264,472084,218635,387924,822826,721243,48162,223686],[63831,118393,693210,662068,312870,402654,15052,291603,556176,368761,243431,285367,941382,14889,821308,855811,322455,670629,687484,784641,862487,702421,979975,224079,675637,193212,273027,831684,658969,309854,695731,738055,795999,248372,48952,841889,270218,97210,591492,632969],[956113,248365,118267,278143,574656,588373,737865,654957,372845,299668,300204,170684,469601,731376,432858,529112,631735,397150,832071,690194,680248,610295,704125,699087,609059,171287,37788,355204,957541,907382,950703,497876,910378,736284,418440,327127,253486,633227,604160,234189],[641099,24216,156365,688716,255700,785462,620717,679491,576736,69254,482491,180763,872660,588345,551445,500576,919209,510992,611833,546653,407444,501332,418282,591025,339370,587831,620450,657430,828307,141305,758375,280101,984812,493666,592396,643954,425593,657651,360806,372209],[379448,688148,353276,737211,274567,213379,333566,1059,925012,720583,291734,584969,873373,421360,391476,172856,241079,658834,449666,610798,304692,640775,705717,656510,879023,286791,399593,511112,775158,462764,945981,182282,204499,445979,968781,238345,455548,23838,810812,972525],[267480,67742,111037,236543,757748,528940,791352,404205,641769,138660,658594,401296,97298,854289,705259,60730,593884,51202,857353,486632,270790,904800,376096,876485,516798,160344,275496,147282,70743,833222,622964,399607,836559,426428,54158,968713,669023,815889,90457,821112],[692833,298337,594003,677972,132572,611228,36338,492292,307083,940003,558467,919197,418533,983799,142407,941958,562510,415337,968408,144490,259368,585468,54727,644729,110695,532776,598530,636199,595736,42650,395915,438021,133487,674448,188274,604630,366122,908317,22391,958095],[102071,529640,106987,721703,731961,224500,925002,45866,229245,4220,919465,244811,519023,241123,268041,41264,122879,130981,640173,127034,607240,630102,298864,912800,185128,433811,822689,564233,230990,528316,834568,549910,353948,928199,469405,869891,546676,344756,275259,402159],[449918,551375,998979,255970,402032,360056,922104,904810,462250,704479,591734,885795,507225,580678,875506,404298,942239,174946,252276,573771,131543,849654,786992,592252,490265,586459,573408,353388,609131,647773,934958,120022,300733,999594,975255,26986,727126,668882,815617,342625],[567929,564420,467228,258506,83917,841865,661405,321428,814309,40166,606179,382937,12868,400539,135101,496974,687294,738153,984757,117774,127872,891573,844977,343863,479727,902947,658676,438489,581355,952882,879778,19260,297807,221954,939150,415389,964409,42142,948163,130880],[388062,425599,258463,618524,48362,245926,402447,97833,408033,346392,69539,935556,131791,54751,665940,420407,319155,89265,647415,729453,685479,831122,987374,97635,135982,892781,105756,203619,691959,273774,553316,910897,859154,558206,823059,419427,225314,958106,362573,441433],[309339,110601,960771,515646,973742,170212,58521,29901,895526,247242,719917,459765,560546,956029,333252,980213,487396,128700,946101,580011,87557,644160,145112,528349,1190,989478,466522,487012,319921,296285,139807,33273,752297,47131,496592,82407,379853,49879,980769,625903]]))
