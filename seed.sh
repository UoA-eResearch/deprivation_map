#!/bin/bash
mkdir seed_progress
for c in BuPu OrRd;do
  for i in AccRank CrimeRank EduRank EmpRank HlthRank HouseRank IncomeRank NZIMDRank;do
    echo $c_$i
    tilestache-seed.py --config tilestache.cfg -b -30 161 -50 179.9 9 10 11 12 13 -l $c_$i -q --progress-file=seed_progress/$i.json &
  done
done
echo all jobs started
