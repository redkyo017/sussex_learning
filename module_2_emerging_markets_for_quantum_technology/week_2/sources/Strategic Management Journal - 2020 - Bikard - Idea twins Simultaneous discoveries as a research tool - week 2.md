# Strategic Management Journal - 2020 - Bikard - Idea twins Simultaneous discoveries as a research tool.epub - week 2
1 | I N T R O D U C T I O N

In 1858, Darwin and Wallace simultaneously published manuscripts describing the process

of evolution through natural selection. A few years later, in 1876, Alexander Bell and Elisha

Gray simultaneously announced the invention of the telephone to the U.S. patent office.

More recently, major breakthroughs such as the discovery of asymptotic freedom in quan-

tum chromodynamics (Politzer, 2005) and that of the CRISPR/Cas9 technology

(Lander, 2016) resulted from a series of findings that often emerged simultaneously from

different labs, raising important questions about the allocation of rewards. Whether in sci-

ence and technology (Hounshell, 1975; Merton, 1961), or even in the arts (McIntosh, 2018),

creative ideas are often not unique. Yet innovation scholars have largely ignored this

phenomenon.

I posit that simultaneous discoveries 1 constitute a useful—and hitherto underexploited— research tool for innovation and strategy research, which makes it possible to investigate two

broad questions. First, what factors shape the exploitation of an innovation? The intrinsic

potential of innovative projects is generally unobservable, opening the door to various theories

and debates. As an example, differences in innovation outcomes may be driven by team size,

but also by differences in the intrinsic potential of the projects on which teams of different size

work (e.g., Singh & Lee Fleming, 2010; Wu, Wang, & Evans, 2019). Simultaneous discoveries

potentially advance the debate because they make it possible to keep the project —and its intrin-

sic potential—(almost) constant across different settings, allowing the researcher to conduct

what amounts to “twin studies of new ideas.”

Second, what drives new ideas? Historical circumstances—the characteristics of a specific

time and place—play an important role in the emergence of new ideas (e.g., Kneeland, Schil-ling, & Aharonson, 2019; Sgourev, 2013). Yet it is often difficult to disentangle the impact of

those circumstances from the role of the innovator. Simultaneous discoveries are a useful way

to tackle this challenge. After all, the variables that are important to the emergence of an idea

are likely to become more salient when observed across multiple settings. Moreover, simulta-

neous discoveries often lead to controversies about the allocation of rewards (Merton, 1961),

which can be useful from a research standpoint because they bring to light norms that may oth-

erwise be taken for granted.

One key reason why this research tool has received little scrutiny over the past few decades

is that few datasets of simultaneous discoveries are available. The last published large-scale list

is almost a century old (Ogburn & Thomas, 1922), and has prompted numerous debates about

the degree of similarity necessary to consider that two ideas are the same (Patinkin, 1983;

Schmookler, 1966). Below I describe a new method to build datasets of simultaneous discoveries

in science, based on Cozzens' (1989) observation that teams of scientists who make the same

discovery must share credit for that discovery, and that credit-sharing is visible in the citations

to the discovery articles in the literature. Building on this insight, I propose a systematic and

automated method to collect a dataset of simultaneous discoveries or “paper twins,” which I make available. I also conduct numerous sensitivity analyses and highlight some of the limita-

tions of this approach.

1 Following the prior literature on this topic (e.g., Merton, 1961; Simonton, 1979) I do not distinguish between different

types of insights — whether scientific discoveries or technological inventions.

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

1530 BIKARD

2 | P R O M I S E S F O R S T R A T E G Y R E S E A R C H

2.1 | What factors shape the exploitation of an innovation?

Innovation is a cumulative process, but the ability of individuals and firms to build on existing

work varies. Innovators fail to exploit new opportunities for many reasons, such as lack of cog-

nitive flexibility (Chai, 2017), lack of prior knowledge (Shane, 2000), or organizational rigidity

(Chesbrough & Rosenbloom, 2002). Missed opportunities can help researchers understand the

drivers of innovation performance, yet are hard to identify because the intrinsic potential of

innovative projects is generally unobserved. As a result, it is difficult to gauge whether the

observed outcome reflects the full potential of innovative projects or falls short.

To clarify the implications of this empirical challenge, consider that we are interested in the

relationship studied by Hounshell (1975) of the link between individual expertise and the

exploitation of new ideas. The impact of expertise β ^ will be given by estimating: 1

Innovation Success ij = β Expertise 1 ij + β X 2 ij + μ , ij

where the success of individual i on innovation project j is a function of individual i's expertise

on project j. X ij is a vector of control variables (e.g., the demographic characteristics of the inno-vator, expected reward for innovation, access to resources, equipment and knowledge, type of

industry or technology), and μ ij is the error term. If the intrinsic potential of project j is not per-

fectly accounted for, the error term can be further decomposed: μ ij = u j + ε ij where u j captures

the unobserved potential of project j and ε ij is the residual variable. Is the assumption that cov

(u j , Expertise ij ) = 0 credible? On average, one might expect that experts choose to work on more promising projects than nonexperts. Thus, depending on the precision of our measure for

intrinsic potential, the chances are high that β ^ will be biased. 1

This empirical challenge is a source of much theoretical debate. For example, if it is

observed that knowledge flows more readily between neighboring firms, how can one deter-

mine whether it is proximity that helps the knowledge flow (Jaffe, Trajtenberg, &

Henderson, 1993), or whether the firms' projects are more relevant to one another

(P. Thompson & Fox-Kean, 2005). Similarly, do firms that collaborate with universities perform

well because of their collaboration (Zucker, Darby, & Armstrong, 2002), or do such collabora-

tions only occur when projects are promising (Lacetera, 2009)?

Current research applies two main approaches to address this challenge. 2 The most com-

mon is probably to use fixed effects, for example at the level of the field (e.g., Lavie &

Drori, 2011; Singh & Fleming, 2010) or of the individual (e.g., Leahey et al., 2017 and Wu

et al., 2019). While this has the advantage of being easy to implement in a large number of set-

tings, it fails to precisely capture the intrinsic potential of innovative projects, and hence the

results may remain hard to interpret. Another approach is to use matching and keyword-based

strategies (e.g., Arts, Cassiman, & Gomez, 2018; Azoulay, Ding, & Stuart, 2009; Kaplan &

2 A number of alternative empirical strategies have been used, in particular the exploitation of specific shocks (L. Zhang, 2016; Jia, Huang, & Zhang, 2018; Huang & Li, 2019). Other approaches include regression discontinuities (e.g., Howell, 2017), instrumental variables (e.g., Galasso & Schankerman, 2014) and randomized control trials (e.g., Boudreau et al., 2016). A comprehensive review of these approaches is beyond the scope of this paper. Those approaches are very powerful, but exogenous shocks, discontinuities, or valid instruments are not always available and randomized control trials are not always possible. I propose that “ twin studies of ideas ” are yet another potentially productive tool for empiricists in settings where simultaneous discoveries are available.

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

BIKARD 1531

Vakili, 2015). These make it possible to identify similar innovative projects in large datasets, yet

they tend to be complicated. Seemingly subtle differences in operationalization can lead to

completely different results (P. Thompson & Fox-Kean, 2005; Henderson, Jaffe, &

Trajtenberg, 2005).

I propose an alternative, complementary approach using simultaneous discoveries as a

research tool. In a sense, such events constitute natural experiments insofar as the same

(or similar) projects are undertaken at around the same time by different innovators. Admit-

tedly, since the projects are essentially the same, their intrinsic potential can be held constant.

Such occurrences are not always observable, but when they are, they provide a natural compari-

son set to study variance in the exploitation of new ideas. Observed differences in the rate or

direction of follow-on innovation are likely to come from the characteristics of the team or the

organization—not from unobserved variance in the projects' intrinsic potential.

Consider the following examples. First, how does expertise shape an individual's ability to

turn an invention into a groundbreaking technology? Answering this question is complicated

by the fact that experts and nonexperts tend to work on different projects. To address this chal-

lenge, David Hounshell (1975) focused on the simultaneous invention of the telephone by Eli-

sha Gray and Alexander Bell. Since both men made essentially the same invention, both could

have pioneered telephone technology. However, Gray's expertise in telegraphic technology

blinded him to the telephone's commercial potential.

Second, how do academic-versus-industrial origins affect inventors' attention to science?

Again, empirical investigation is difficult because universities tend to work on projects that are

more fundamental, on average, than firms. Simultaneous discoveries can be used to hold the

intrinsic potential of academic and industrial science constant. Using this approach,

Bikard (2018) found that inventors paid less attention to discoveries “made in academia.”

These are just two examples of how simultaneous discoveries and inventions can be used to

undertake “twin studies of new ideas”—that is, holding the innovative project constant to con-trol for the unobserved variance in its intrinsic potential. Future studies might examine the

impact of age, of belonging to a minority, or of specific training, social status, or network struc-

ture. They might also examine the impact of team size and composition, as well as that of orga-

nizational characteristics such as incentive structures, resources or location (e.g., Bikard &

Marx, 2019; Bikard, Vakili, & Teodoridis, 2019; Marx & Hsu, 2019). Concretely, one could build

a dataset of instances in which immigrant and nonimmigrant scientists made the same discov-

ery, and then explore whether immigrants exploit new ideas differently from locals. Doing so

might deepen our understanding of the relationship between immigration and innovation.

2.2 | What drives new ideas?

2.2.1 | Historical circumstances

I propose that simultaneous discoveries are a useful research tool to study the role of historical

circumstances in the innovation process. Those circumstances can, admittedly, be studied in

cases where no twin is observed, as with the emergence and dynamics of the partnership system

in Renaissance Florence (Padgett & McLean, 2006), Cubism in 19th-century Paris

(Sgourev, 2013), the biotechnology industry in the United States in the late 1970s and 1980s

(Zucker, Darby, & Brewer, 1998), or high fashion in New York, London, Milan and Paris in the

early 21st century (Godart & Galunic, 2019). However, in these types of studies, researchers

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

1532 BIKARD

typically observe one particular idea emerging in one setting, or different ideas emerging in var-

ious settings, which makes it difficult to assess which characteristics of the setting (if any) drove

the emergence of a specific breakthrough. One advantage of using twins is that the link

between setting characteristics and idea may become clearer.

A sizeable body of literature is based on this approach. Such studies have been referred to as

“Zeitgeist theories of creativity” (Simonton, 1986; Stokes, 1986) because they consider that

simultaneous discoveries and inventions are signs that “the time must be ripe” (Kuhn, 1959,

p. 321), or that some ideas were “in the air” (Lamb & Easton, 1984, p. 173) at a specific time and place. These studies apply two types of empirical strategies.

One group conducts historical studies (e.g., Constant, 1978; Kuhn, 1959; Niehans, 1995). For

example, Kuhn (1959) argues that energy conservation emerged as a simultaneous discovery in

the early 19th century thanks to scientific advances, widespread concern about engines, and the

popularity of Naturphilosophie at the time. Strikingly, the German-speaking world, where

Naturphilosophie was particularly influential, made a disproportionate contribution to the dis-

covery. In his study of the alleged independent inventions of the steam turbines and Pelton

water wheels, Constant (1978) also emphasizes cognitive drivers of new ideas such as paradig-

matic commitments and shared standards and ideologies, and points to the role of technological

co-evolution whereby technological developments not only enable but call for new complemen-

tary technologies.

Another group studies quantitative patterns in the emergence of simultaneous discoveries

and inventions, exploring the role of chance, timing and location in innovation. For example,

de Solla Price (1965) and Simonton (1979) highlight that the emergence of twins, triplets, qua-

druplets (and so forth) appear to follow a Poisson distribution. This indicates that nulltons—

cases where new ideas could have emerged but did not—are frequent, and that chance there-fore plays an important role in the emergence of new ideas. More recently, Ganguli, Lin, and

Reynolds (2020) use patent interferences to show that collocated inventors are more likely to

produce simultaneous inventions than more distant ones, consistent with the view that knowl-

edge spillovers are localized. Similarly, Baruffaldi and Raffo (2017) use citations to overlapping

inventions in European patent data to show that individuals working within a short distance

are more likely to produce overlapping ideas early on, whereas over time, the “reinvention of

the wheel” is more likely among distant inventors.

2.2.2 | The allocation of rewards

Another potential use of simultaneous discoveries as a research tool arises because such events

often cast light on difficult-to-observe norms in the allocation of rewards for innovation. When

individuals or teams have similar ideas around the same time, each may claim that they are

entitled to the reward. Others may argue that the simultaneous nature of the discovery suggests

it had become obvious. Where there is ambiguity about the merits of their respective claims,

tensions may surface in scientific discourse and in the media (Merton, 1961). H. David Politzer,

who shared the 2004 Nobel Prize for Physics with David Gross and Frank Wilczek for their

independent discovery of asymptotic freedom in quantum chromodynamics, described this ten-

sion in his Nobel lecture:

The neat, linear progress, as outlined by the sequence of gleaming gems recognized

by Nobel Prizes, is a useful fiction. But a fiction it is. The truth is often far more

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

BIKARD 1533

complicated. Of course, there are the oft-told priority disputes, bickering over who

is responsible for some particular idea. But those questions are not only often

unresolvable, they are often rather meaningless. Genuinely independent discovery

is not only possible, it occurs all the time. (Politzer, 2005, p. 86)

That same tension sometimes degenerates into a major controversy or legal battle for owner-

ship of intellectual property rights, as in the case of the battle opposing the MIT-Harvard Broad

Institute and UC Berkeley about the CRISPR-Cas9 gene editing technology (S. Zhang, 2015).

When simultaneous discoveries occur, the allocation of rewards often prompts debate about

otherwise implicit and taken-for-granted rules and norms. Cozzens (1989), for example, exam-

ined social control and credit allocation in science through an in-depth qualitative study of the

discovery of the opiate receptor by four teams between 1971 and 1973. Since no two scientific

papers are ever identical, she sought to understand why the scientific community decided that

this was a case of scientific multiples. She found that credit for a discovery was shared (or not)

through a collective process. The scientific community's view on the equivalence of two or more

contributions surfaced as each scientist took a stance both privately and publicly in their pre-

sentations and publications.

Future studies might examine the impact of paradigm strength or of the emergence of new

tools and needs on the occurrence of simultaneous discoveries and inventions. They might also

examine variance in their emergence across different fields, for example, between science and

technology, or even in the arts. Others might investigate what drives the emergence of contro-

versies in cases of simultaneous discoveries and how they affect individuals and organizations.

Concretely, one could consider a set of simultaneous discoveries in the same field and then

investigate which ones led to conflict, which did not, and why. Doing so may deepen our under-

standing of the relationship between creativity and conflict.

3 | A M E T H O D F O R B U I L D I N G A D A T A S E T O F

#### S I M U L T A N E O U S D I S C O V E R I E S

3.1 | Identifying simultaneous discoveries

The largest and most studied list of simultaneous discoveries and inventions to date is probably

Ogburn and Thomas's (1922) list of 148 instances. This and other, unpublished ones

(Merton, 1961; Simonton, 1979) were compiled from historical records, and have therefore been

criticized as subjective, unsystematic and unreproducible. Merton and Merton (1968, pp. 9–10)

noted: “It is no easy matter to establish the degree of similarity between independently devel-oped ideas. Even in the more exact disciplines, such as mathematics, claims of independent

multiple inventions are vigorously debated. The question is, how much overlap should be taken

to constitute ‘identity’?” While a few researchers have suggested specific criteria to do so, they generally admit that those criteria cannot be applied consistently by different people across dif-

ferent settings (Elkana, 1971; Patinkin, 1983). As Niehans (1995, p. 7) puts it: “Multiple discov-

eries are a ‘fuzzy set’, and the harder one tries to delineate it, the fuzzier it looks.”

Yet, while every scientific paper is different, scientists appear to know when discoveries are

equivalent. It is striking to note how frequently scientists claim that they have been forestalled.

In a survey, Hagstrom (1974), for instance, found that more than 60% of the 1,718 U.S. scientists

he surveyed declared having been anticipated by another scientist in the publication of a

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

1534 BIKARD

discovery at least once in their career. Merton and Merton (1968, p. 10) noted that “another kind of evidence seems presumptive if not compelling evidence of identity or equivalence: the

report of a later discoverer that another had arrived there before him. Presumably, these reports

are truthful since the modern age of science puts a premium on originality.” While there are presumably an infinite number of ways to make a discovery and to describe it, the credit allo-

cated for a discovery is finite; scientists have a sense about whether two discoveries are equiva-

lent from a credit standpoint.

I propose that one can infer whether two discoveries are essentially the same by observing

how credit is allocated. When mentioning a simultaneous discovery in a paper or a presenta-

tion, scientists may decide to split the credit by citing all the co-discoverers adjacently or in the

same parenthesis, since citations are a critical currency in the cycle of scientific credit

(Latour & Woolgar, 1986). In her study of the simultaneous discovery of the opiate receptor,

Cozzens (1989) noted: “The interviews with third parties indicated that a close examination of what was said about the co-discoveries when they were cited would say something about the

extent of consensus.” Cozzens's interviewees described proper citation as a “moral obligation,”

as well as “a way of expressing one's own viewpoint” in the debate about who deserves credit

(Cozzens, 1989, pp. 120 –21). Citations can therefore be used as measure of the votes of the sci-

entific community on whether two papers are twins—that is, whether they share the credit for the same discovery.

This approach has two important implications. First, it does not give a clear answer about

what counts or does not count as a twin. Consensus about credit allocation is a continuous vari-

able, not a discrete one. Researchers must choose how they define what counts as twins

depending on their research question (as discussed in Section 3.3). Second, it cannot capture

the entire universe of simultaneous discoveries. There may be a false negative, for example, if

individuals or teams do not receive the credit they deserve. I discuss this and other limitations

in Section 3.4.

3.2 | The algorithm

The method described below generates datasets of pairs of scientific papers that share credit for

the same discovery —here operationalized as “paper twins”—in a systematic and transparent manner. To ensure reproducibility, I use only publicly available data from PubMed. The algo-

rithm involves three main steps.

Step 1 consists of building a set of pairs of articles. To do so, the algorithm considers all

29,247,013 articles included in PubMed between 1960 and 2018. 3 Each article in PubMed is

paired with the top 10 most similar articles according to PubMed's keyword-based “Similar arti-

cle ” list. Pairs are excluded if each paper has not received at least five citations in PubMed, if there is no overlap in the set of citing papers, if the pairs have at least one author in common,

and if the papers were published more than 1 calendar year apart. This produces 4,048,393

In Step 2, the Jaccard Index for each pair is computed. The Jaccard Index is a set-theoretic

measure consisting of the fraction of the intersection of the two sets of citations divided by their

union. It is described in section A1 of this paper's Appendix S1. Figure 1 shows that the Jaccard

3 Those data were collected in August 2019.

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

BIKARD 1535

F I G U R E 1 Distribution of the pairs by Jaccard Index value \[Color figure can be viewed at

wileyonlinelibrary.com\]Index for the 4,048,393 pairs is highly skewed. I define as potential twins only those pairs hav-

ing a Jaccard Index above 50%. This leaves 32,240 pairs.

Step 3 consists in identifying those among the 32,240 pairs for which co-citation takes place

systematically adjacently, or in the same parentheses, which indicates that credit for the discov-

ery is split. Overall, those pairs have 492,534 co-citing articles. Full text was available in open

access through PubMed for 105,435 (21%) of those. Pairs for which the full text of fewer than

three co-citing articles could be observed were removed, leaving 10,927 pairs. These constitute

the final set of potential paper twins. The list is published on the FIVES open-access website

(http://five.dartmouth.edu/datasets). The distribution of adjacent co-citation rates is plotted in

This algorithm includes a number of thresholds and cutoff points, which raises the question

of how modifying those thresholds would affect the final dataset. I explore this issue and con-

duct a number of sensitivity analyses in section A2 of this paper's Appendix (Supporting

Information).

3.3 | Within-pair similarity

The fact that two scientific discoveries are never exactly the same may raise concerns that subtle

within-pair differences could still constitute a source of bias. Below, I describe four measures of

within-pair similarity (also published together with the dataset) which make it possible to con-

duct sensitivity analyses by using different thresholds for what counts as twin.

3.3.1 | Rate of adjacent co-citation

This is the key measure of within-pair similarity on which the above algorithm relies. The rate

of adjacent co-citation constitutes a measure of a field's consensus that credit ought to be

shared. This measure is not perfect, as teams might not always receive the credit that they

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

1536 BIKARD

F I G U R E 2 Distribution of the 10,927 finalist “ potential twin papers ” by level of adjacent co-citation \[Color

figure can be viewed atwileyonlinelibrary.com\]deserve. Still, the more often co-citations happen adjacently, the more similar paper twins will

probably be, on average.

3.3.2 | Semantic similarity

I used the PubMed list of “Similar articles” to assess semantic similarity. For each article in its database, PubMed publishes the list of the most similar articles. To do so, a word-weighted algo-

rithm examines similarity in the words from the article's title, abstract, and Medical Subject

Headings (Lin & Wilbur, 2007). For each paper, the best matches in the full PubMed library are

precalculated and stored as a set. For example, by the end of 2017, PubMed included over

27 million papers. For a paper to be less than 10 ranks away from another paper published at

the time means that it would be in the top 0.00004% most similar article in the PubMed data-

base. I build a semantic similarity score for each pair of papers by examining the average rank

of paper A in paper B's similar article list, and vice versa.

3.3.3 | Publication-month difference

The same discovery can be made by different teams months or years apart (Merton, 1961). In

addition, there is always variance in the pace at which journals, reviewers and authors handle

the review process. At the same time, if the discoveries are really the same, a manuscript is

unlikely to be accepted by a journal if another has already been published. This is why scientists

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

BIKARD 1537

rush to publish. Thus, in the case of frequently co-cited papers, months' difference is likely to

measure within-pair similarity.

3.3.4 | Back-to-back publication

Scientists involved in simultaneous discoveries may decide to submit their findings to the same

journal. Sometimes submission is even synchronized so that there is less chance of one team

being forestalled by the other. When this happens, editors who feel that both teams deserve

credit frequently decide to publish the two manuscripts back to back. From their perspective,

this is a way to ensure that the credit is split and also provides reassuring evidence that a find-

ing is replicable. In the case of frequently co-cited papers that do not have shared authors,

back-to-back publication provides evidence that two papers are disclosing the same discovery.

Table 1 illustrates the dataset as well as those measures in the case of three simultaneous

discoveries that were awarded the Nobel Prize in Physiology or Medicine respectively in 1975,

1993, and 2019. I examine the relationship between rate of adjacent co-citation and the other

three measures of with-pair similarity in Table 2. To do so, I split the dataset of 10,927 pairs into

four subsamples. For each subsample, I measure within-pair similarity by examining semantic

similarity, publication-month difference, and the occurrence of back-to-back publication. This

analysis shows that different pairs have different similarity levels. Researchers using these data

should assess the level of similarity that they need depending on their research questions.

In some cases, expert panels can also be used to measure within-pair similarity in a granular

way. Bikard (2018), for instance, investigated within-pair similarity in a sample of paper twins

in which at least one paper came from a university and the other came from a firm. To do so,

he recruited 10 postdoctoral researchers in the corresponding fields and asked them to qualita-

tively analyze and codify these differences. The most common difference noted by those experts

was in the level of detail, but they also noted variance in practical emphasis, in the richness of

the theory, in their level of sophistication, and in their clarity.

3.4 | Method's limitations and boundary conditions

The approach described above has four main limitations, which constrain the use of these types

of data and open up potential avenues for future research. First, the dataset published with this

paper is relatively small. It includes 10,927 pairs of potential twins. While the figure is much

higher than Ogburn and Thomas's (1922) list of 148 instances, it is small compared to the size

of the scientific literature. Moreover, researchers interested in using these data will unavoidably

focus on a subset of cases. For example, those seeking to study the commercialization of science

might choose to exclude fundamental discoveries. The relatively small size of the dataset natu-

rally puts a limit on the number of questions that can be answered using these data. Over time,

researchers might be able to create larger samples by taking advantage of scientific journals'

increasing tendency to make the full text of articles available online (which is important for

Step 3 of the algorithm). Moreover, the approach described in this paper could also be used to

collect lists of simultaneous discoveries from other data sources, such as the Web of Science or

Microsoft Academics.

Second, this method cannot capture the entire universe of simultaneous discoveries. Since it

was collected using PubMed, it focuses on the biomedical and life sciences literature. There

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

1538 BIKARD

Back-to-back (yes 1 0 1

Av. difference 15.5

Month difference 0 1 0

Rate adjacent co-citation (%) 82 87 83

Jaccard Index 76 60 53

or J. for of α , S. R. DNA Rous RNA. 5516: 902310) HIF , of 226 E., ends erts, 0 sequence R. 5 292 4316301) 11292862) 2001. Physiology Rob the Mizutani, Nature (PMID: proline Implications virions in & al. at messenger 8 & in 2 – et VHL-mediated by Science (PMID: Gelinas, R., amazing 1 virus. Prize M., (PMID: for T. RNA-dependent T., An (1), H. 1213 2 – L. 12 468. Mircea, sensing. – Nobel 2 (1970). polymerase sarcoma 1211 Broker, (1977). arrangement adenovirus Cell targeted destruction hydroxylation: O 464

the Paper Temin, Chow, Ivan,

that in 0 of (8), al. 5 A. 74 et - late P. Natl von 2 (1970). the O 5516: Moore, 2 , (PMID: (PMID: , RNA at of prolyl twins D. USA the by (PMID: viruses. of M., Proc Panu, Lindau 226 Spliced Targeting 292 to – polymerase 1211 S. Sharp, Sci 3175 1 – – α 472. & paper –

of RNA-dependent DNA virions tumour Nature 1209 4316300) C., (1977). segments terminus adenovirus mRNA. Acad 3171 269380) (2001). HIF- Hippel ubiquitylation complex regulated hydroxylation. Science 468 11292861)

Paper Baltimore, Berget, Jaakkola,

1 Nobel Prize) Nobel

transcription (1975 Prize) Nobel hydroxylation (2019 Prize)

Discovery Reverse Split Prolyl

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

BIKARD 1539

T A B L E 2 Rate of adjacent co-citation and within-pair similarity

25 – 50% 50 – 75% 75 – 100%

0 – 25% adjacent adjacent adjacent adjacent co-citation co-citation co-citation co-citation

n = 1,705 n = 2,200 n = 3,672 n = 3,846

Mean SD Mean SD Mean SD Mean SD

Jaccard Index 0.57 0.09 0.57 0.09 0.58 0.09 0.59 0.09

Month difference a 7.83 5.58 7.50 5.76 6.39 5.64 5.09 5.55

Rank difference 4.21 2.78 3.84 2.72 3.42 2.63 2.92 2.45

Back-to-back publication a 0.04 0.20 0.05 0.22 0.10 0.30 0.17 0.38

a Month difference and back-to-back publication could not be computed for all pairs. For month difference,

n = 1,503 for 0 – 25%, n = 1,934 for 25 – 50%, n = 3,355 for 50 – 75%, and n = 3,529 for 75 – 100% bracket. For back-to-back publication, n = 1,699 for 0 – 25%, n = 2,192 for 25 – 50%, n = 3,655 for 50 – 75%, and n = 3,828 for 75 – 100% bracket.

may be false negatives if teams do not receive the credit that they deserve, which could happen

for example if one team does not publish their findings, or if they are an outsider to a scientific

community. Moreover, the same approach cannot be used to identify “twin patents” because the process of citation in patents is very different from that of citations in scientific articles, and

because two patents cannot be awarded to different teams for the same invention in the same

country. Other methods may be developed over time to build similar datasets in other settings

(Baruffaldi & Raffo, 2017; Hill & Stein, 2019; Ganguli et al., 2020; N. Thompson & Kuhn, 2020).

Many scientific discoveries are never published and many inventions are never patented, yet

scientific paper and patent data are widely used by innovation researchers because they are

useful—though imperfect—proxies for discovery and invention (Criscuolo, Alexy, Sharapov, & Salter, 2019; Mukherjee & Stern, 2009). I propose that paper twins can similarly be used as an

imperfect but useful proxy for simultaneous discoveries in science.

Third, when using twin data obtained by this approach, researchers should not use variance

in citations (credit) received by the twin papers as the dependent variable of interest. This is a

direct consequence of the fact that those simultaneous discoveries were identified because of

their high rate of co-citation. Instead, these data might be used to examine the antecedents of

those discoveries, conflict in sharing credit, or follow-on innovation by the co-discoverers or

other inventors, for example.

Fourth, the extent to which the results obtained studying twins generalize to nontwins is

not always clear. The frequency of simultaneous discoveries is a matter of some debate. At one

extreme, Merton (1961, p. 477) famously argued that “All scientific discoveries are in principle

multiples. ” They appear as singletons because we are unable to observe the twins, not because those twins do not exist. Other scholars have claimed, however, that such events are the excep-

tion, not the rule (Schmookler, 1966). If this is true, one might worry that innovators act differ-

ently in cases of simultaneous discoveries compared with other cases, perhaps because

competition induces them to do so (Katila & Chen, 2008; Toh & Polidoro, 2013). This makes it

harder to interpret results obtained using twin data. As an example, it is clear that Elisha Gray

missed the telephone opportunity because Alexander Bell seized it, but it is impossible to gauge

what Gray would have done had Bell not existed.

10970266, 2020, 8, Downloaded from https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3162 by University Of Sussex Library, Wiley Online Library on \[25/07/2026\]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

1540 BIKARD

4 | C O N C L U S I O N

Simultaneous discoveries are a useful research tool for strategy and innovation research. This

paper attempts to facilitate their use in three ways. First, it describes questions that might be

explored using this research tool and reviews prior work on this topic. One broad set of ques-

tions relates to the factors shaping the exploitation of innovation. By holding the innovation

(almost) constant, simultaneous discoveries make it possible to conduct what amounts to twin

studies of new ideas. Using those events, researchers can compare how and why different indi-

viduals and organizations exploit (or fail to exploit) the same or very similar ideas. Another

broad set of questions examines the historical circumstances leading to the emergence of new

ideas as well as the allocation of rewards for those ideas.

Second, it describes a method that makes it possible to collect lists of recent simultaneous

discoveries in a systematic and automated way. To ensure ease of replication, the algorithm

exploits only publicly available sources. It is based on Cozzens's (1989) insight that teams that

make the same discovery often share credit for it—and that credit-sharing is visible in the rate of adjacent co-citations in the follow-on scientific literature.

Third, I provide the dataset collected using this method (seehttp://five.dartmouth.edu/datasets),which has not been used to date. It includes four measures of within-pair similarity

so that researchers can decide how they wish to define paper twins and can easily conduct sen-

sitivity analyses.

In his 1963 article on scientific multiples as a research setting, Merton noted that the idea of

independent discovery is confirmed by its own history, since it has been “periodically

rediscovered over a span of centuries” (Merton, 1963, p. 237). This essay is not a rediscovery of the idea of simultaneous discoveries. Rather, it is an attempt to answer Merton's half-century-

old call to recognize that these events offer tremendous research opportunities for social

scientists.