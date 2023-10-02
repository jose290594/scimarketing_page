from dash import (
    Dash, 
    html, 
    Input, 
    Output, 
    State,
    ALL,
    callback,
    clientside_callback,
    no_update
)
from dash.dcc import Input as dcc_input, Tooltip as dcc_tooltip
from flask.app import Flask
import regex as re
import time

#estilos de la aplicacion
external_stylesheets = [
    #'assets/public/animate/cdnjs.cloudflare.com_ajax_libs_animate.css_4.1.1_animate.css',
]
#scripts externos
external_scripts = [
    #'assets/public/custom/main_script.js'
]

services_dict = {
    'Market Research and Segmentation' : {
        'title': 'Market Research and Segmentation',
        'description': '',
        'img': 'assets/icons/chart-pie-svgrepo-com.svg',
    },
    'Buyer Persona Development' : {
        'title': 'Buyer Persona Development',
        'description': '',
        'img': 'assets/icons/cart-check-svgrepo-com.svg',
    },
    'Email Marketing' : {
        'title': 'Email Marketing',
        'description': '',
        'img': 'assets/icons/mail-svgrepo-com.svg',
    },
    'Marketing Automation' : {
        'title': 'Marketing Automation',
        'description': '',
        'img': 'assets/icons/settings-svgrepo-com.svg',
    },
    'CRM and Lead Management' : {
        'title': 'CRM and Lead Management',
        'description': '',
        'img': 'assets/icons/chart-pie-alt-svgrepo-com.svg',
    },
    'B2B Influencer Marketing' : {
        'title': 'B2B Influencer Marketing',
        'description': '',
        'img': 'assets/icons/campaign-svgrepo-com.svg',
    },
    'Landing Page and Form Development' : {
        'title': 'Landing Page and Form Development',
        'description': '',
        'img': 'assets/icons/folder-code-svgrepo-com.svg',
    },
    'Analytics and Reporting' : {
        'title': 'Analytics and Reporting',
        'description': '',
        'img': 'assets/icons/chart-line-alt-1-svgrepo-com.svg',
    },
}

#Servidor Flask
server = Flask('sci_marketing_page')

app = Dash(
    name='SCI Marketing page', 
    title='SCI Marketing', 
    update_title="Leading...",
    suppress_callback_exceptions = True, 
    external_stylesheets = external_stylesheets,
    #external_scripts=external_scripts,
    assets_folder='assets',
    
    meta_tags = [
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ], 
    server = server, #type:ignore
)

app.layout = html.Div(
    [
        html.Button(
            '<', 
            className="carousel-arrow prev", 
            id='prev'
        ),
        html.Button(
            '>', 
            className="carousel-arrow next", 
            id='next'
        ),
        html.Div(
            [
                #Recibimiento
                html.Div(
                    [
                        html.Div(
                            'SCI', 
                            className='sci-title-1 animate__animated animate__fadeInDown'
                        ),
                        html.Iframe(
                            src='assets/img/logo-sci-marketing.svg', 
                            className='sci-logo animate__animated animate__rotateIn'
                        ),
                        html.Div(
                            'Marketing', 
                            className='sci-title-2 animate__animated animate__fadeInUp'
                        ),
                    ], className='sci-slide sci-slide-1',
                    style={
                        'background-image': 'url(assets/bg/lineardrop.svg)',
                        'background-size': 'cover',
                        'background-position': 'center',
                        'background-repeat': 'no-repeat',
                    }
                ),
                #Introduccion
                html.Div(
                    [
                        #slogan
                        html.Div(
                            [
                                html.Div('Reach', className='sci-word sci-slogan-1'),
                                html.Div('To', className='sci-word sci-slogan-2'),
                                html.Div('The', className='sci-word sci-slogan-3'),
                                html.Div('Ones', className='sci-word sci-slogan-4'),
                                html.Div('That', className='sci-word sci-slogan-5'),
                                html.Div('Matters', className='sci-word sci-slogan-6'),
                            ], className='sci-intro-1 sci-slogan'
                        ),
                        #texto
                        html.Div(
                            [
                                html.P(
                                    """
                                        At SCI Marketing, we're dedicated to 
                                        helping your business thrive in the 
                                        competitive B2B landscape. Our mission 
                                        is simple: to supercharge your growth 
                                        by delivering high-quality leads that 
                                        drive results. We specialize in B2B 
                                        lead generation, providing a 
                                        comprehensive suite of services tailored 
                                        to your unique needs. From market 
                                        research and content strategy to 
                                        targeted outreach and lead nurturing, 
                                        we have the expertise to fuel your 
                                        sales pipeline with qualified prospects.
                                    """.replace('\n', '')),
                            ], className='sci-intro-2 sci-slogan',
                            
                        )
                    ], className='sci-slide sci-slide-2',
                    style={
                        'background-image': 'url(assets/bg/diagonalrain.svg)',
                        'background-size': 'cover',
                        'background-position': 'center',
                        'background-repeat': 'no-repeat',
                    }
                ),
                
                #Servicios
                html.Div(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src=service[1]['img'], 
                                    className='sci-service-img'
                                ),
                                html.Div(
                                    service[1]['title'], 
                                    className='sci-service-title'
                                ),
                            ], className='sci-service-card',
                            id={
                                'type': 'sci-service-card', 
                                'index': service[1]['title']
                            }
                        )
                        for service in services_dict.items()
                    ]+[
                        dcc_tooltip(id="graph-tooltip", className="sci-tooltip"),
                    ], className='sci-slide sci-slide-3',
                    style={
                        'background-image': 'url(assets/bg/lateralrain.svg)',
                        'background-size': 'cover',
                        'background-position': 'center',
                        'background-repeat': 'no-repeat',
                    }
                ),
                # #Case Studies
                # html.Div(
                #     [
                #     ], className='sci-slide sci-slide-4',
                # ),
                #Contact
                html.Div(
                    [
                        html.Div(
                            [
                                html.H1(
                                    "Contact Us",
                                    style={
                                        'text-align':'center',
                                        'font-weight':'900',
                                    }
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Label(
                                                    "Name", 
                                                    className="sci-form-label",
                                                ),
                                                dcc_input(
                                                    type="text", 
                                                    id="sci-name-form", 
                                                    placeholder="Enter a name...",
                                                    required=True,
                                                    style={'border-radius': '3px'}
                                                ),
                                            ],
                                            className="",
                                            style={'display': 'grid'}
                                        ),
                                        html.Div(
                                            [
                                                html.Label(
                                                    "Email", 
                                                    className="sci-form-label",
                                                ),
                                                dcc_input(
                                                    type="email", 
                                                    id="sci-email-form", 
                                                    placeholder="Enter an email to get in touch...",
                                                    required=True,
                                                    style={'border-radius': '3px'}
                                                ),
                                            ],
                                            className="",
                                            style={'display': 'grid'}
                                        ),
                                        html.Div(
                                            [
                                                html.Label(
                                                    "Message",
                                                    className="sci-form-label",
                                                ),
                                                html.Textarea(
                                                    id="sci-msg-form", 
                                                    placeholder="write about what your needs are...",
                                                    style={'border-radius': '4px'}
                                                ),
                                            ],
                                            className="",
                                            style={'display': 'grid'}
                                        ),
                                        html.Button(
                                            children="Send", 
                                            id="sci-submit-button",
                                            style={
                                                "font-weight": "900",
                                                "font-style": "italic",
                                                "z-index": "5",
                                            }
                                        ),
                                    ], 
                                    className="""
                                        sci-contact-form
                                    """,                            
                                ),
                                html.A(
                                    'Or',
                                    style={
                                        'width':'100%',
                                        'text-align':'center'
                                    }
                                ),
                                html.A(
                                    '''Contact us directly via email to 
                                    contact@sci.marketing''',
                                    href="mailto:contact@sci.marketing",
                                    style={
                                        'width':'100%',
                                        'text-align':'center'
                                    }
                                )

                            ], className="""
                                sci-container-form
                            """,
                        ),

                    ], className='sci-slide sci-slide-5',
                    style={
                        'background-image': 'url(assets/bg/othersiderain.svg)',
                        'background-size': 'cover',
                        'background-position': 'center',
                        'background-repeat': 'no-repeat',
                    }
                ),
            ], className='main-container',
            id='main-container'
        ),
        html.Script("""
            let scrollContainer = document.getElementById('main-container')
            let scrollLeftButton = document.getElementById('prev')
            let scrollRightButton = document.getElementById('next')

            scrollLeftButton.addEventListener('click', scrollLeft)
            scrollRightButton.addEventListener('click', scrollRight)

            function scrollLeft() {

                console.log("scrolling left")
                scrollContainer.scrollBy({
                    left: -scrollContainer.clientWidth,
                    behavior: 'smooth',
                })
            }

            function scrollRight() {
                console.log("scrolling left")
                scrollContainer.scrollBy({
                    left: scrollContainer.clientWidth,
                    behavior: 'smooth',
                })
            }
        """),
    
    ], style={
        'overflow-x': 'hidden',
        'overflow-y': 'hidden',
    }
)


@callback(
    [Output("sci-submit-button", "children"),
    Output("sci-submit-button", "disabled"),],
    [Input("sci-submit-button", "n_clicks"),],
    [State("sci-name-form", "value"),
    State("sci-email-form", "value"),
    State("sci-msg-form", "children"),],
    prevent_initial_call=True,
)
def ask_for_help(n_clicks, name, email, msg):
    if n_clicks > 0:
        if name and email:
            #remove special characters but keep spaces, letters, numbers, @ and .
            name = re.sub(r'[^\w\s]', '', name)
            email = re.sub(r'[^\w\s]', '', email)
            msg = re.sub(r'[^\w\s]', '', str(msg))
            body = f"""{name}\n{email}\n{msg}"""
            #open a file and write the body
            help_request = open(f'{name}-{str(int(time.time()))}-help_request.txt', 'w')
            help_request.write(body)
            help_request.close()

            return "SENT!", True
        else:
            return "Error or field missing!", False
    else:
        return "Send", False

@callback(
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "children"),
    Input({"type": "sci-service-card", "index":ALL}, "n_clicks"),
    [State({"type": "sci-service-card", "index":ALL}, "id"),],
    prevent_initial_call=True,
)
def display_hover(nclicks, service):
    if service is None:
        return False, no_update, no_update
    children = [
        html.Div([
            html.H3(str(service)),
        ], style={'width': '200px', 'white-space': 'normal'})
    ]

    return True, children


clientside_callback(
    """
    function() {
        let scrollContainer = document.getElementById('main-container')

        ctx = dash_clientside.callback_context.triggered[0].prop_id
        
        if (ctx == 'prev.n_clicks') {
            scrollContainer.scrollBy({
                left: -scrollContainer.clientWidth,
                behavior: 'smooth',
            })
            return dash_clientside.no_update
        }
        
        if (ctx == 'next.n_clicks') {
            scrollContainer.scrollBy({
                left: scrollContainer.clientWidth,
                behavior: 'smooth',
            })
            return dash_clientside.no_update
        }
    }
    """,
    Output("main-container", "children"),
    Input("prev", "n_clicks"),
    Input("next", "n_clicks"),
    prevent_initial_call=True,
)

if __name__ == '__main__':
    app.run_server('0.0.0.0', debug=True)