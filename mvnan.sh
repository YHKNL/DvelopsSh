#!/bin/bash
#判断当前脚本是否为绝对路径，匹配以/开头下的所有
:<<'COMMENT'
if [[ $0 =~ ^\/.* ]] ; then
  script=$0
else
  script=$(pwd)/$0
fi

#获取文件的真实路径
script=`readlink -f $script`
#获取文件所在的目录
script_path=${script%/*}
#获取文件所在目录的真实路径
realpath=$(readlink -f $script_path)
cd $realpath

# install maven
echo "----------------------install maven start---------------------------"
wget http://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.tar.gz
tar -zvxf apache-maven-3.6.1-bin.tar.gz
mv apache-maven-3.6.1 /usr/local/maven3
COMMENT
mavenHome=`cat /etc/profile |grep 'export MAVEN_HOME='`
if [ "$mavenHome" == "" ]; then
   echo 'export MAVEN_HOME=/usr/local/maven3/apache-maven-3.6.1'>>/etc/profile
   echo 'export PATH="${MAVEN_HOME}/bin:$PATH"'>>/etc/profile
   source /etc/profile
fi

echo $(mvn -v)
echo "--------------------------install maven end----------------------------------"
