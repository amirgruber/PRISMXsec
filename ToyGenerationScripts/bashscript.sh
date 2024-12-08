#!/bin/bash
count=0
for i in $(seq 0 999)
do
#  echo "Running toy${i}"
  condor_submit /afs/cern.ch/work/a/amgruber/public/ToyGen/ToyGenSubmit.sub -append "arguments = ${i}"
  count=$((count+1))
  if [ $count -eq 100 ]
  then
    echo "Done submitting ${i}"
    count=0
  fi
done
echo "Finished submitting all jobs"
