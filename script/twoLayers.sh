#!/bin/sh
# AUTHOR:   yaolili
# FILE:     twoLayers.sh
# ROLE:     TODO (some explanation)
# CREATED:  2015-11-28 14:36:50
# MODIFIED: 2015-11-29 10:54:45


first="$(date +"%T")"

inputPath="../data/testSample/sampleText/output"
outputPath="../data/testSample/sampleOutput/test"

dfs()
{
    for file in `ls $1`
    do  
        if [ -d $1"/"$file ]
        then
            local path=$1"/"$file
            dfs $path
        else
            local path=$1"/"$file
            local name=$file
            local output=$outputPath"/"${1#*${inputPath}/}
            python preprocessing/twoLayers.py ${output}/${name}.entity.txt ${output}/${name}.entity.twoLayers.txt
        fi  
    done
}

dfs $inputPath

end="$(date +"%T")"
echo $first-$end
