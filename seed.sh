#!/bin/bash
mkdir seed_progress
for c in BuPu OrRd RdYlGn;do
  for i in AccRank CrimeRank EduRank EmpRank HlthRank HouseRank IncomeRank NZIMDRank;do
    name=${c}_${i}
    echo $name
    tilestache-seed.py --config tilestache.cfg -b -30 161 -50 179.9 9 10 11 12 13 -l $name -q --progress-file=seed_progress/$name.json &
  done
done
name=LINZ_Residential
echo $name
tilestache-seed.py --config tilestache.cfg -b -30 161 -50 179.9 9 10 11 12 13 -l $name -q --progress-file=seed_progress/$name.json &
echo all jobs started
