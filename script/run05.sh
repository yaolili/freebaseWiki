#!/bin/sh
#
# The script takes a single parameter -- the ../Config filename

first="$(date +"%T")"

jar="./dist/wikifier-3.0-jar-with-dependencies.jar"
inputPath="./data/testSample/sampleText/Q05"
outputPath="./data/testSample/sampleOutput/test"
config="./configs/STAND_ALONE_GUROBI.xml"

dfs()
{
    for file in `ls $1`
    do
        if [ -d $1"/"$file ]
        then
            local path=$1"/"$file
            #mkdir $outputPath"/"${path#*${inputPath}/}
            dfs $path
        else
            local path=$1"/"$file
            local name=$file
            local output=$outputPath"/"${1#*${inputPath}/}
            #echo $output
            #java -Xmx8G -jar ${jar} -annotateData ${path} ${output}/ false ${config} 
            python preprocessing/run.py ${output}/${name}.wikification.tagged.full.xml ${output}/${name}.entity.txt
            #exit 0
        fi
    done
}

dfs $inputPath

#java -Xmx10G -jar ${jar} -annotateData ${inputPath}/test.txt ${outputPath} false ${config}
#python preprocessing/run.py ${outputPath}/test.txt.wikification.tagged.full.xml out.txt

end="$(date +"%T")"
echo $first-$end
