<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="/struts-tags" prefix="s" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %> 
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Success Page</title>
</head>
<body>
    <h1>现有信息:</h1> <br/>
 		<s:form action="register3" method="post">
    	 <s:textfield label="站点名字" name="website.name" tooltip="站点名字 如：百度"></s:textfield>
    	 <s:textfield label="频道地址" name="website.channel" tooltip="频道的url地址"></s:textfield>
    	<s:submit label="Register"   value="删除" />
    	<s:submit label="Register"  action="register4"  value="修改" />
    	<s:submit label="Register"  action="quit"  value="返回" />
    	</s:form>
    	
    <c:forEach items="${webs}" var="list">
    	<s:form action="register4" method="post">
    	
    	 ${list.name} <br>
    	 <s:textfield label="站点名字改为" name="website.name" tooltip="站点名字 如：百度"></s:textfield>
        ${list.channel} <br>
        <s:textfield label="频道地址改为" name="website.channel" tooltip="频道的url地址"></s:textfield>
        ${list.region}<br>
        <s:select name="website.region" list="#{'Territory':'境内','Abroad':'境外'}" label="境内外" headerKey="Territory" headerValue="选择境内外"></s:select>
        ${list.contry}<br>
        <s:select name="website.contry" list="#{'CN':'中国','US':'美国','JP':'日本','UK','英国'}" label="国家" headerKey="CN" headerValue="选择国家"></s:select>
        ${list.language}<br>
        <s:select name="website.language" list="#{'CN':'中文','US':'英文','JP':'日文'}" label="语言" headerKey="CN" headerValue="选择语言"></s:select>
        <br />
        <!-- 
        <s:textfield label="start_time" name="website.start_time"></s:textfield>
        <s:textfield label="stop_time" name="website.stop_time" tooltip="age must over 16"></s:textfield>
         -->
        ${list.title}<br>
        <s:textfield label="文章标题的path改为" name="website.title" tooltip="标签"></s:textfield>
        ${list.author}<br>
        <s:textfield label="文章作者的path改为" name="website.author" tooltip="标签"></s:textfield>
        ${list.pubtime}<br>
        <s:textfield label="发布时间的path改为" name="website.pubtime" tooltip="i标签"></s:textfield>
        ${list.content}<br>
        <s:textfield label="正文的path改为" name="website.content" tooltip="标签"></s:textfield>
        ${list.source}<br>
        <s:textfield label="转发来源的path改为" name="website.source" tooltip="标签"></s:textfield>
		<br />
		.......................................
       <s:select name="website.region" list="#{'turn':'是','false':'否'}" label="禁用" headerKey="false" headerValue="选择"></s:select>
        <s:submit  value="修改"></s:submit>  
   		<s:submit  action="register6"  value="测试" ></s:submit>  
    	
		</s:form>
    </c:forEach>

</body>
</html>