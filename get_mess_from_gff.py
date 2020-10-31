
import sys
import Make_Transcript_Class

fr_gff_file_in = "temp.gff"

transcript_mess_dir = {}


with open(fr_gff_file_in, 'r') as fr_gff_file:
    for i in fr_gff_file:
        if i.startswith('#'):
            continue
        else:
            items = i.strip().split('\t')
            if items[2] == "gene":
                gene_id = items[-1].split(';')[0].split("ID=")[1]
            elif items[2] == "mRNA":
                transcript_id = items[-1].split(';')[0].split("ID=")[1]
                transcript_mess_dir[transcript_id] = Make_Transcript_Class.Make_Transcript_Class(items[6], gene_id, transcript_id)
            elif items[2] == "five_prime_UTR":
                five_prime_UTR_start_site = int(items[3])
                five_prime_UTR_end_site = int(items[4])
                five_prime_UTR_mess = (five_prime_UTR_start_site, five_prime_UTR_end_site)
                transcript_mess_dir[transcript_id].UTR_mess.append(five_prime_UTR_mess)
            elif items[2] == "exon":
                exon_start_site = int(items[3])
                exon_end_site = int(items[4])
                exon_mess = (exon_start_site, exon_end_site)
                transcript_mess_dir[transcript_id].exon_mess.append(exon_mess)
            elif items[2] == "three_prime_UTR":
                three_prime_UTR_start_site = int(items[3])
                three_prime_UTR_end_site = int(items[4])
                three_prime_UTR_mess = (three_prime_UTR_start_site, three_prime_UTR_end_site)
                transcript_mess_dir[transcript_id].UTR_mess.append(three_prime_UTR_mess)
            elif items[2] == "CDS":
                CDS_start_site = int(items[3])
                CDS_end_site = int(items[4])
                CDS_mess = (CDS_start_site, CDS_end_site)
                transcript_mess_dir[transcript_id].CDS_mess.append(CDS_mess)


print(len(transcript_mess_dir))
print(transcript_mess_dir["BMSK10000080.1"].transcript_id)
print(len(transcript_mess_dir["BMSK10000080.1"].exon_mess))