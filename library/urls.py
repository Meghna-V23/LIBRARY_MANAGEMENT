from django.urls import path

from library import views

from django.urls import path

from library import views

urlpatterns = [
    path('',views.login,name="login"),
    path('log', views.log,name="log"),

    path('add_and_mangelibrary', views.add_and_mangelibrary, name="add_and_mangelibrary"),
    path('edit_library/<int:id>', views.edit_library, name="edit_library"),
    path('edit_lib',views.edit_lib, name="edit_lib"),
    path('deletelibrary/<int:id>',views.deletelibrary, name="deletelibrary"),
    path('add_library',views.add_library, name="add_library"),
    path('add_lib',views.add_lib, name="add_lib"),


    path('admin_home', views.admin_home, name="admin_home"),
    path('library_home', views.library_home, name="library_home"),

    path('library_reg', views.library_reg, name="library_reg"),
    path('libreg', views.libreg, name="libreg"),


    path('managebook_lib', views.managebook_lib, name="managebook_lib"),
    path('editbooks1/<int:id>', views.editbooks1, name="editbooks1"),
    path('edit_books', views.edit_books, name="edit_books"),
    path('deletebooks/<int:id>', views.deletebooks, name="deletebooks"),
    path('addbooks', views.addbooks, name="addbooks"),
    path('addbooks1', views.addbooks1, name="addbooks1"),

    path('send_complaint', views.send_complaint, name="send_complaint"),

    path('s_complaint', views.s_complaint, name="s_complaint"),

    path('sendrating_user', views.sendrating_user, name="sendrating_user"),
    path('usrrating', views.usrrating, name="usrrating"),


    path('sendreply_lib', views.sendreply_lib, name="sendreply_lib"),
    path('userhome', views.userhome, name="userhome"),

    path('userreg', views.userreg, name="userreg"),
    path('usrrg', views.usrrg, name="usrrg"),

    path('verifylibrary', views.verifylibrary, name="verifylibrary"),
    path('Accept_library/<int:id>', views.Accept_library, name="Accept_library"),
    path('Reject_library/<int:id>', views.Reject_library, name="Reject_library"),

    path('viewbook_adm', views.viewbook_adm, name="viewbook_adm"),

    path('viewbooks_user/<int:id>', views.viewbooks_user, name="viewbooks_user"),

    path('viewcomplaintreply_user', views.viewcomplaintreply_user, name="viewcomplaintreply_user"),

    path('viewlib_and_books', views.viewlib_and_books, name="viewlib_and_books"),

    path('viewrating_lib', views.viewrating_lib, name="viewrating_lib"),

    path('viewratinglibrary_adm', views.viewratinglibrary_adm, name="viewratinglibrary_adm"),

    path('viewuser_adm', views.viewuser_adm, name="viewuser_adm"),


    path('viewcomplaintsndrply_lib', views.viewcomplaintsndrply_lib, name="viewcomplaintsndrply_lib"),
    path('sendreply_lib/<int:id>', views.sendreply_lib, name="sendreply_lib"),
    path('sndrplylib', views.sndrplylib, name="sndrplylib"),





]