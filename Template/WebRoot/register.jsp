<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="/struts-tags" prefix="s" %>
<!DOCTYPE HTML>
<!--
	Helios 1.0 by HTML5 UP
	html5up.net | @n33co
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Helios by HTML5 UP</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600" rel="stylesheet" type="text/css" />
		<!--[if lte IE 8]><script src="js/html5shiv.js"></script><![endif]-->
		<script src="js/jquery.min.js"></script>
		<script src="js/jquery.dropotron.js"></script>
		<script src="js/skel.min.js"></script>
		<script src="js/skel-panels.min.js"></script>
		<script src="js/init.js"></script>
		<script type="text/javascript" src='js/f.js'></script>
		<noscript>
			<link rel="stylesheet" href="css/skel-noscript.css" />
			<link rel="stylesheet" href="css/style.css" />
			<link rel="stylesheet" href="css/style-desktop.css" />
			<link rel="stylesheet" href="css/style-noscript.css" />
		</noscript>
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie8.css" /><![endif]-->
	</head>
	<script>baidu("120x270")</script>
	<body class="homepage">

		<!-- Header -->
			<div id="header">
						
				<!-- Inner -->
					<div class="inner">
						<header>
							<h1><a href="#" id="logo">Helios</a></h1>
							<hr />
							<span class="byline">Another fine freebie by HTML5 UP</span>
						</header>
						<footer>
							<a href="start.action" class="button circled scrolly">Start</a>
						</footer>
					</div>
				
				<!-- Nav -->
					<nav id="nav">
						<ul>
							<li><a href="index.html">Home</a></li>
							<li>
								<span>Dropdown</span>
								<ul>
									<li><a href="#">Lorem ipsum dolor</a></li>
									<li><a href="#">Magna phasellus</a></li>
									<li><a href="#">Etiam dolore nisl</a></li>
									<li>
										<span>And a submenu &hellip;</span>
										<ul>
											<li><a href="#">Lorem ipsum dolor</a></li>
											<li><a href="#">Phasellus consequat</a></li>
											<li><a href="#">Magna phasellus</a></li>
											<li><a href="#">Etiam dolore nisl</a></li>
										</ul>
									</li>
									<li><a href="#">Veroeros feugiat</a></li>
								</ul>
							</li>
							<li><a href="left-sidebar.html">Left Sidebar</a></li>
							<li><a href="right-sidebar.html">Right Sidebar</a></li>
							<li><a href="no-sidebar.html">No Sidebar</a></li>
						</ul>
					</nav>

			</div>
			
		
		<!-- Footer -->
			<div id="footer">
				<div class="container">
					<div class="row">
						<s:fielderror />
						<s:form action="register" method="post">
						
							<section class="4u">
							<s:textfield label="站点名字" name="website.name" tooltip="站点名字 如：百度"></s:textfield>
        					<s:textfield label="频道地址" name="website.channel" tooltip="频道的url地址"></s:textfield>
        					<s:select name="website.region" list="#{'Territory':'境内','Abroad':'境外'}" label="境内外" headerKey="Territory" headerValue="选择境内外" ></s:select>
        					<s:select name="website.contry" list="#{'CN':'中国','US':'美国','JP':'日本','UK','英国'}" label="国家" headerKey="CN" headerValue="选择国家" ></s:select>
        					<s:select name="website.language" list="#{'CN':'中文','US':'英文','JP':'日文'}" label="语言" headerKey="CN" headerValue="选择语言" ></s:select>
					        <br />
					        <!-- 
					        <s:textfield label="start_time" name="website.start_time"></s:textfield>
					        <s:textfield label="stop_time" name="website.stop_time" tooltip="age must over 16"></s:textfield>
					         -->
					        <s:textfield label="文章标题的path" name="website.title" tooltip="标签"></s:textfield>
					        <s:textfield label="文章作者的path" name="website.author" tooltip="标签"></s:textfield>
					        <s:textfield label="发布时间的path" name="website.pubtime" tooltip="i标签"></s:textfield>
					        <s:textfield label="正文的path" name="website.content" tooltip="标签"></s:textfield>
					        <s:textfield label="转发来源的path" name="website.source" tooltip="标签"></s:textfield>
							<br />
					        <s:submit label="Register" value="录入"></s:submit>  
					   		<s:submit label="Register" action="register2"  value="查看" ></s:submit>  
					  				
							</section>

						</s:form>
					</div>
					<hr />
					<div class="row">
						<div class="12u">
							
							<!-- Contact -->
								<section class="contact">
									<header>
										<h3>Nisl turpis nascetur interdum?</h3>
									</header>
									<p>Urna nisl non quis interdum mus ornare ridiculus egestas ridiculus lobortis vivamus tempor aliquet.</p>
									<ul class="icons">
										<li><a href="#" class="icon icon-twitter"><span>Twitter</span></a></li>
										<li><a href="#" class="icon icon-facebook"><span>Facebook</span></a></li>
										<li><a href="#" class="icon icon-google-plus"><span>Google+</span></a></li>
										<li><a href="#" class="icon icon-pinterest"><span>Pinterest</span></a></li>
										<li><a href="#" class="icon icon-dribbble"><span>Dribbble</span></a></li>
										<li><a href="#" class="icon icon-linkedin"><span>Linkedin</span></a></li>
									</ul>
								</section>
							
							<!-- Copyright -->
								<div class="copyright">
									<ul class="menu">
										<li>&copy; Untitled. All rights reserved.</li>
										<li>中科瑞特大数据 | 天津市大学软件学院</li>
										<li>Demo Images: <a href="http://mdomaradzki.deviantart.com/">Michael Domaradzki</a></li>
									</ul>
								</div>
							
						</div>
					
					</div>
				</div>
			</div>

	</body>
</html>