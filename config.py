
sourcedir = '../house-styles/'
dircss = 'static/css/'
dirless = 'static/css/less/'
dirjs = 'static/js/'

lessfile = 'styles.less'
responsivelessfile = 'styles-responsive.less'

'''
Notes
- name is used for display purposes in the generator
- id is used for the form variables, must be unique and contain no spaces
- less is the full name of the less file
- responsive is the full name of the responsive less file
- including responsive option as same as regular less file means that file will also be incorporated into responsive styles, which for the house styles is needed for variables and mixins
- type must be either 'core', 'extra' or 'optional'
- styleg is currently unused
- js is currently unused
'''

files = [
    #core files
    {   'name': "Typography",
        'id': "type",
        'less': "type.less",
        'styleg': "typography.html",
        'type':"core"
    },
    {   'name': "Clearfix",
        'id': "clearfix",
        'less': "clearfix.less",
        'type':"core"
    },
    {   'name': "Media",
        'id': "media",
        'less': "media.less",
        'styleg': "media.html",
        'type':"core"
    },
    {   'name': "Mixins",
        'id': "mixins",
        'less': "mixins.less",
        'type':"core",
        'responsive':"mixins.less"
    },
    {   'name': "Page",
        'id': "page",
        'less': "page.less",
        'type':"core"
    },
    {   'name': "Reset",
        'id': "reset",
        'less': "reset.less",
        'type':"core"
    },
    {   'name': "Variables",
        'id': "variables",
        'less': "variables.less",
        'styleg': "variables.html",
        'type':"core",
        'responsive':"variables.less"
    },



    #extra files
    {   'name': "Breadcrumbs",
        'id': "breadcrumbs",
        'less': "breadcrumbs.less",
        'styleg': "breadcrumbs.html",
        'type':"extra"
    },
    {   'name': "Buttons",
        'id': "buttons",
        'less': "buttons.less",
        'styleg': "buttons.html",
        'type':"extra"
    },
    {   'name': "Footer",
        'id': "footer",
        'less': "footer.less",
        'type':"extra"
    },
    {   'name': "Forms",
        'id': "forms",
        'less': "forms.less",
        'styleg': "forms.html",
        'responsive':"forms-responsive.less",
        'type':"extra"
    },
    {   'name': "Grid",
        'id': "grid",
        'less': "grid.less",
        'styleg': "grid.html",
        'responsive':"grid-responsive.less",
        'type':"extra"
    },
    {   'name': "Header",
        'id': "header",
        'less': "header.less",
        'type':"extra"
    },
    {   'name': "Links",
        'id': "links",
        'less': "links.less",
        'styleg': "links.html",
        'type':"extra"
    },
    {   'name': "Lists",
        'id': "lists",
        'less': "lists.less",
        'styleg': "lists.html",
        'type':"extra"
    },
    {   'name': "Nav",
        'id': "nav",
        'less': "nav.less",
        'styleg': "nav.html",
        'type':"extra"
    },
    {   'name': "Tables",
        'id': "tables",
        'less': "tables.less",
        'styleg': "tables.html",
        'type':"extra"
    },
    {   'name': "Utility",
        'id': "utility",
        'less': "utility.less",
        'styleg': "utility.html",
        'js': "",
        'type':'extra'
    },
    {   'name': "Wells",
        'id': "wells",
        'less': "wells.less",
        'styleg': "wells.html",
        'js': "",
        'type':'extra'
    },



    #optional files
    {   'name': "Alerts",
        'id': "alerts",
        'less': "alerts.less",
        'styleg': "alerts.html",
        'js': "alerts.js",
        'type':"optional"
    },
    {   'name': "Button groups",
        'id': "button-groups",
        'less': "button-groups.less",
        'styleg': "button-groups.html",
        'js': "button-groups.js",
        'type':"optional"
    },
    {   'name': "Popups",
        'id': "popups",
        'less': "popups.less",
        'styleg': "popups.html",
        'js': "popups.js",
        'responsive': "popups-responsive.less",
        'type':"optional"
    },
    {   'name': "Tabs",
        'id': "tabs",
        'less': "tabs.less",
        'styleg': "tabs.html",
        'js': "",
        'responsive':"tabs-responsive.less",
        'type':"optional"
    },

]

