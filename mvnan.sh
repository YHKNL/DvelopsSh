#!/bin/bash
#�жϵ�ǰ�ű��Ƿ�Ϊ����·����ƥ����/��ͷ�µ�����
:<<'COMMENT'
if [[ $0 =~ ^\/.* ]] ; then
  script=$0
else
  script=$(pwd)/$0
fi

#��ȡ�ļ�����ʵ·��
script=`readlink -f $script`
#��ȡ�ļ����ڵ�Ŀ¼
script_path=${script%/*}
#��ȡ�ļ�����Ŀ¼����ʵ·��
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
