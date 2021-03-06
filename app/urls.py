"""valweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from app import views

urlpatterns = [
    path('about/', views.about, name='about'),

    path('Importer/', views.index, name='index'),
    path('Exporter/', views.index2, name='index2'),
    path('Bank/', views.index3, name='index3'),
    path('Shipper/', views.index4, name='index4'),

    path('charts/', views.charts, name='charts'),
    path('charts/', views.charts, name='charts2'),
    path('charts/', views.charts, name='charts3'),
    path('charts/', views.charts, name='charts4'),

    path('LCR/', views.ing, name='ing'),
    path('OS/', views.ing2_1, name='ing2_1'),
    path('SR/', views.ing2_2, name='ing2_2'),
    path('CI/', views.ing2_3, name='ing2_3'),
    path('LC/', views.ing3, name='ing3'),
    path('BL/', views.ing4_1, name='ing4_1'),
    path('DO/', views.ing4_2, name='ing4_2'),

    path('transfer/', views.transfer2_1, name='transfer2_1'),
    path('osdetail/', views.osdetail, name='osdetail'),



    path('remove/', views.remove, name='remove'),
    path('remove2_1/', views.remove2_1, name='remove2_1'),
    path('remove2_2/', views.remove2_2, name='remove2_2'),
    path('remove2_3/', views.remove2_3, name='remove2_3'),
    path('remove3/', views.remove3, name='remove3'),
    path('remove4_1/', views.remove4_1, name='remove4_1'),
    path('remove4_2/', views.remove4_2, name='remove4_2'),


    path('LCR_form/', views.forms, name='forms'),
    path('OS_form/', views.forms2_1, name='forms2_1'),
    path('SR_form/', views.forms2_2, name='forms2_2'),
    path('CI_form/', views.forms2_3, name='forms2_3'),
    path('LC_form/', views.forms3, name='forms3'),
    path('BL_form/', views.forms4_1, name='forms4_1'),
    path('DO_form/', views.forms4_2, name='forms4_2'),

    path('submit/', views.submit, name='submit'),
    path('submit2_1/', views.submit2_1, name='submit2_1'),
    path('submit2_2/', views.submit2_2, name='submit2_2'),
    path('submit2_3/', views.submit2_3, name='submit2_3'),
    path('submit3/', views.submit3, name='submit3'),
    path('submit4_1/', views.submit4_1, name='submit4_1'),
    path('submit4_2/', views.submit4_2, name='submit4_2'),

    path('share1/', views.share1, name='share1'),
    path('share2_1/', views.share2_1, name='share2_1'),
    path('share2_2/', views.share2_2, name='share2_2'),
    path('share2_3/', views.share2_3, name='share2_3'),
    path('share3/', views.share3, name='share3'),
    path('share4_1/', views.share4_1, name='share4_1'),
    path('share4_2/', views.share4_2, name='share4_2'),

    path('OS_received/', views.osreceived, name='osreceived'),
    path('BL_received_I/', views.blreceived1, name='blreceived1'),
    path('BL_received_E/', views.blreceived2, name='blreceived2'),
    path('BL_received_B/', views.blreceived3, name='blreceived3'),
    path('DO_received/', views.doreceived, name='doreceived'),
    path('SR_received/', views.srreceived, name='srreceived'),
    path('CI_received/', views.cireceived, name='cireceived'),
    path('LC_received_I/', views.lcreceived1, name='lcreceived1'),
    path('LC_received_E/', views.lcreceived2, name='lcreceived2'),
    path('LCR_received/', views.lcrreceived, name='lcrreceived'),

    path('os_reject/', views.os_reject, name='os_reject'),
    path('lcr_reject/', views.lcr_reject, name='lcr_reject'),
    path('lc_reject/', views.lc_reject, name='lc_reject'),
    path('sr_reject/', views.sr_reject, name='sr_reject'),
    path('bl_reject/', views.bl_reject, name='bl_reject'),
    path('ci_reject/', views.ci_reject, name='ci_reject'),
    path('do_reject/', views.do_reject, name='do_reject'),

    path('os_confirm/', views.os_confirm, name='os_confirm'),
    path('lcr_confirm/', views.lcr_confirm, name='lcr_confirm'),
    path('lc_confirm/', views.lc_confirm, name='lc_confirm'),
    path('sr_confirm/', views.sr_confirm, name='sr_confirm'),
    path('bl_confirm/', views.bl_confirm, name='bl_confirm'),
    path('bl_confirm1/', views.bl_confirm1, name='bl_confirm1'),
    path('bl_confirm2/', views.bl_confirm2, name='bl_confirm2'),
    path('ci_confirm/', views.ci_confirm, name='ci_confirm'),
    path('do_confirm/', views.do_confirm, name='do_confirm'),


    path('blremove1/', views.blremove1, name='blremove1'),
    path('blremove2/', views.blremove2, name='blremove2'),
    path('blremove3/', views.blremove3, name='blremove3'),
    path('lcremove1/', views.lcremove1, name='lcremove1'),
    path('lcremove2/', views.lcremove2, name='lcremove2'),
    path('doremove/', views.doremove, name='doremove'),
    path('lcrremove/', views.lcrremove, name='lcrremove'),
    path('ciremove/', views.ciremove, name='ciremove'),
    path('osremove/', views.osremove, name='osremove'),
    path('srremove/', views.lcrremove, name='srremove'),

    path('download/', views.download, name='download'),
    path('download2_1/', views.download2_1, name='download2_1'),
    path('download2_2/', views.download2_2, name='download2_2'),
    path('download2_3/', views.download2_3, name='download2_3'),
    path('download3/', views.download3, name='download3'),
    path('download4_1/', views.download4_1, name='download4_1'),
    path('download4_2/', views.download4_2, name='download4_2'),

    path('', views.login, name='login'),
    path('registerpage', views.registerpage, name='registerpage'),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name='forgot'),
    path('logout/', views.logout, name='logout'),


    path('search1/', views.search1, name='search1'),
    path('search2/', views.search2, name='search2'),
    path('search3/', views.search3, name='search3'),
    path('search4/', views.search4, name='search4'),

    path('mypage1/', views.mypage1, name='mypage1'),
    path('mypage2/', views.mypage2, name='mypage2'),
    path('mypage3/', views.mypage3, name='mypage3'),
    path('mypage4/', views.mypage4, name='mypage4'),

    path('makeotp/', views.makeotp, name='makeotp'),

    path('pwmodify/', views.pwmodify, name='pwmodify'),

    path('addressmodify/', views.addressmodify, name='addressmodify'),

    path('checkcontract/', views.checkcontract, name='checkcontract'),

    path('checkid/', views.checkid, name='checkid'),

    path('mytrade/', views.mytrade, name='mytrade'),
    path('email/', views.email, name='email'),
    path('user_manual/', views.user_manual, name='user_manual'),

]
