from django.shortcuts import render

def index(request):
    context = {
        'reseña': "Somos una empresa líder en reclutamiento, dedicada a conectar talentos excepcionales con empresas innovadoras. Nos especializamos en entender las necesidades únicas de cada cliente y candidato para crear oportunidades de crecimiento mutuo. Nuestro enfoque se basa en la integridad, la eficiencia y un profundo conocimiento del mercado laboral. Trabajamos incansablemente para asegurar que cada proceso de selección sea un éxito para todas las partes involucradas, construyendo relaciones duraderas basadas en la confianza y el respeto.",
        'mision': "Nuestra misión es empoderar a individuos y organizaciones, facilitando la búsqueda del ajuste perfecto entre el talento y las oportunidades laborales. Nos esforzamos por ser el socio estratégico de confianza en el desarrollo de carreras y el crecimiento empresarial, a través de soluciones de reclutamiento personalizadas y de alta calidad que impulsen el éxito.",
        'vision': "Aspiramos a ser la principal plataforma de reclutamiento a nivel nacional, reconocida por nuestra innovación, ética y excelencia en el servicio. Buscamos transformar la industria del reclutamiento a través de la tecnología y un enfoque centrado en las personas, creando un ecosistema donde el talento y las oportunidades convergen de manera fluida y efectiva para todos.",
    }
    return render(request, 'app_enzocopto/index.html', context)

def personal(request):
    equipo = [
        {
            'nombre': 'Andrea Salazar', 'cargo': 'Gerente General',
            'descripcion': 'Lidera la empresa con una visión estratégica y un profundo conocimiento del mercado. Con más de 15 años de experiencia en el sector, Andrea se enfoca en expandir nuestros servicios y mantener la excelencia en cada proyecto. Su compromiso con el desarrollo de talentos es la piedra angular de nuestra filosofía de trabajo.',
            'imagen1': 'imagen_1_personal.jpg', 'imagen2': 'imagen_2_personal.jpg'
        },
        {
            'nombre': 'Marcos Pérez', 'cargo': 'Director de Operaciones',
            'descripcion': 'Encargado de optimizar los procesos internos y asegurar la eficiencia operativa. Marcos implementa las mejores prácticas para garantizar un servicio ágil y de alta calidad. Su habilidad para resolver problemas y su atención al detalle son clave para el éxito de nuestras operaciones diarias y la satisfacción de nuestros clientes.',
            'imagen1': 'imagen_3_personal.jpg', 'imagen2': 'imagen_4_personal.jpg'
        },
        {
            'nombre': 'Sofía Rojas', 'cargo': 'Jefa de Reclutamiento',
            'descripcion': 'Experta en identificar y atraer a los mejores candidatos. Sofía tiene un ojo clínico para el talento y una red de contactos inigualable en diversas industrias. Ella lidera nuestro equipo de reclutadores para encontrar a las personas adecuadas para cada vacante, garantizando siempre el mejor ajuste cultural y profesional.',
            'imagen1': 'imagen_5_personal.jpg', 'imagen2': 'imagen_6_personal.jpg'
        },
        {
            'nombre': 'Javier Muñoz', 'cargo': 'Analista de Datos',
            'descripcion': 'Responsable de analizar tendencias del mercado laboral y métricas de reclutamiento. Javier utiliza los datos para optimizar nuestras estrategias y predecir las necesidades futuras de nuestros clientes. Su trabajo asegura que nuestras decisiones se basen en información sólida y actualizada para ofrecer siempre los mejores resultados.',
            'imagen1': 'imagen_7_personal.jpg', 'imagen2': 'imagen_8_personal.jpg'
        },
        {
            'nombre': 'Valeria Soto', 'cargo': 'Asesora de Carreras',
            'descripcion': 'Guía a los candidatos en su desarrollo profesional, brindando consejos sobre currículums, entrevistas y planes de carrera. Valeria ayuda a los talentos a presentarse de la mejor manera y a alcanzar sus objetivos. Su empatía y conocimiento del mercado son invaluables para quienes buscan un cambio significativo en sus vidas.',
            'imagen1': 'imagen_9_personal.jpg', 'imagen2': 'imagen_10_personal.jpg'
        },
    ]
    context = {'equipo': equipo}
    return render(request, 'app_enzocopto/personal.html', context)

def clientes(request):
    clientes_list = [
        {
            'nombre': 'Innovatech Solutions', 'profesion_oficio': 'Tecnología',
            'reseña': 'Gracias a su equipo de reclutamiento, encontramos a los ingenieros de software que necesitábamos para un proyecto clave. Su proceso fue rápido y eficiente, identificando candidatos que no hubiéramos encontrado por nuestra cuenta.',
            'imagen': 'imagen_1_clientes.jpg'
        },
        {
            'nombre': 'Vitalis Center', 'profesion_oficio': 'Salud',
            'reseña': 'La calidad de los profesionales de la salud que nos presentaron superó nuestras expectativas. La empresa entendió a la perfección la cultura de nuestra organización y las habilidades específicas que buscábamos para nuestro equipo.',
            'imagen': 'imagen_2_clientes.jpg'
        },
        {
            'nombre': 'CreativaMente Digital', 'profesion_oficio': 'Marketing',
            'reseña': 'Para nuestra última campaña, necesitábamos un equipo de marketing digital con habilidades muy específicas. La empresa nos ayudó a encontrar a los creativos y analistas perfectos que se integraron sin problemas.',
            'imagen': 'imagen_3_clientes.jpg'
        },
        {
            'nombre': 'Quantum Capital', 'profesion_oficio': 'Finanzas',
            'reseña': 'Buscábamos un perfil muy especializado en finanzas corporativas y su equipo nos presentó a los candidatos más calificados. Su proceso de selección fue riguroso y transparente, lo que nos dio total confianza en su trabajo.',
            'imagen': 'imagen_4_clientes.jpg'
        },
        {
            'nombre': 'Educa Futuro', 'profesion_oficio': 'Educación',
            'reseña': 'Para nuestro centro educativo, era vital encontrar educadores con una gran vocación y experiencia. La empresa de reclutamiento nos ayudó a identificar a los candidatos que no solo tenían las credenciales correctas, sino también la pasión por la enseñanza.',
            'imagen': 'imagen_5_clientes.jpg'
        },
        {
            'nombre': 'Punto Urbano', 'profesion_oficio': 'Retail',
            'reseña': 'Nuestra expansión requería la contratación de personal clave para la gestión de nuevas tiendas. La empresa nos proporcionó un servicio rápido y efectivo, presentándonos a gerentes y supervisores con gran potencial.',
            'imagen': 'imagen_6_clientes.jpg'
        },
        {
            'nombre': 'Logixpress Global', 'profesion_oficio': 'Logística',
            'reseña': 'Encontramos a los especialistas en logística que necesitábamos para optimizar nuestra cadena de suministro. Su equipo entendió perfectamente los desafíos de nuestro sector y nos ofreció soluciones de personal que han tenido un impacto directo.',
            'imagen': 'imagen_7_clientes.jpg'
        },
        {
            'nombre': 'Vector Proyectos', 'profesion_oficio': 'Ingeniería',
            'reseña': 'La empresa nos conectó con ingenieros de proyectos con la experiencia técnica y las habilidades de liderazgo que eran esenciales para nuestro trabajo. El proceso de selección fue meticuloso y los resultados han sido fantásticos.',
            'imagen': 'imagen_8_clientes.jpg'
        },
        {
            'nombre': 'Procesa Industrial', 'profesion_oficio': 'Manufactura',
            'reseña': 'Para nuestra planta de producción, necesitábamos personal técnico altamente calificado. La empresa de reclutamiento nos ayudó a encontrar a los operarios y supervisores con la experiencia necesaria para garantizar la calidad.',
            'imagen': 'imagen_9_clientes.jpg'
        },
        {
            'nombre': 'Nexus Devs', 'profesion_oficio': 'Tecnología',
            'reseña': 'Nexus Devs se ha convertido en un socio clave para nuestra empresa tecnológica. Siempre nos proporcionan a los mejores ingenieros, diseñadores y gerentes de proyecto, con perfiles de un nivel muy alto.',
            'imagen': 'imagen_10_clientes.jpg'
        },
    ]
    context = {'clientes': clientes_list}
    return render(request, 'app_enzocopto/clientes.html', context)

def egresados(request):
    egresados_list = [
        {
            'nombre': 'Juan Gómez', 'empresa': 'Tech Solutions',
            'opinion': 'Gracias a su asesoría, pude preparar mi currículum y mi entrevista de la mejor manera. Me sentí seguro y listo para enfrentar el proceso de selección. Hoy, gracias a su apoyo, trabajo en una de las empresas de tecnología más innovadoras del país. Su guía fue fundamental para lograr mi primer empleo formal.',
            'imagen': 'imagen_1_egresados.jpg'
        },
        {
            'nombre': 'Ana Torres', 'empresa': 'Health Corp',
            'opinion': 'Me ayudaron a encontrar una posición que se ajustaba perfectamente a mis habilidades y mi pasión por el sector salud. Me proporcionaron los contactos y el apoyo necesario para destacar en un mercado competitivo. La empresa se convirtió en mi puente hacia una carrera profesional sólida y exitosa.',
            'imagen': 'imagen_2_egresados.jpg'
        },
        {
            'nombre': 'Pedro Vargas', 'empresa': 'Marketing Global',
            'opinion': 'El equipo de reclutamiento entendió mi perfil y mis aspiraciones, presentándome a una empresa de marketing donde he podido crecer profesionalmente. Su seguimiento y consejos fueron clave para mi éxito. Recomiendo totalmente su servicio a cualquiera que esté buscando un cambio significativo en su carrera profesional.',
            'imagen': 'imagen_3_egresados.jpg'
        },
        {
            'nombre': 'Claudia Ríos', 'empresa': 'Financial Group',
            'opinion': 'Como egresada, no sabía por dónde empezar mi búsqueda de empleo. Su servicio me dio la dirección y las herramientas que necesitaba. Hoy, me desempeño en una de las firmas financieras más prestigiosas, algo que no hubiera logrado sin su ayuda y constante apoyo.',
            'imagen': 'imagen_4_egresados.jpg'
        },
        {
            'nombre': 'Felipe Soto', 'empresa': 'Future Education',
            'opinion': 'Mi paso por el proceso de selección fue mucho más sencillo gracias a la empresa. Me prepararon para la entrevista y me conectaron con la oportunidad ideal. Su dedicación y compromiso con mi éxito profesional me impresionó. Hoy, estoy muy feliz y me siento realizado en mi trabajo como profesor.',
            'imagen': 'imagen_5_egresados.jpg'
        },
        {
            'nombre': 'Rosa Morales', 'empresa': 'Retail Dynamics',
            'opinion': 'Me proporcionaron una guía clara y consejos prácticos que marcaron la diferencia en mi búsqueda de empleo. Me sentí apoyada en todo momento y el resultado fue una excelente oferta de trabajo en el sector del retail. Su profesionalismo y atención al detalle me hicieron sentir muy especial.',
            'imagen': 'imagen_6_egresados.jpg'
        },
        {
            'nombre': 'Luis Castro', 'empresa': 'Logistics Solutions',
            'opinion': 'El equipo me ayudó a encontrar un puesto que no solo se ajustaba a mi formación, sino que también me ofrecía un camino de crecimiento. Su conocimiento del mercado y su red de contactos son impresionantes. Me siento muy afortunado de haber contado con su apoyo en esta etapa.',
            'imagen': 'imagen_7_egresados.jpg'
        },
        {
            'nombre': 'Elena Jiménez', 'empresa': 'Engineering Corp',
            'opinion': 'Me ayudaron a dar el salto de estudiante a profesional, conectándome con una de las empresas de ingeniería más importantes. Su preparación para la entrevista fue exhaustiva y me dio la confianza necesaria para brillar. Sin su ayuda, este logro no habría sido posible en tan poco tiempo.',
            'imagen': 'imagen_8_egresados.jpg'
        },
    ]
    context = {'egresados': egresados_list}
    return render(request, 'app_enzocopto/egresados.html', context)