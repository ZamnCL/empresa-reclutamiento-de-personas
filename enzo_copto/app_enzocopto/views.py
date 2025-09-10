from django.shortcuts import render

def index(request):
    """
    Vista para la página de inicio (index.html).
    Pasa datos de la empresa (reseña, misión, visión) a la plantilla.
    """
    context = {
        'reseña': "Somos una empresa líder en reclutamiento, dedicada a conectar talentos excepcionales con empresas innovadoras. Nos especializamos en entender las necesidades únicas de cada cliente y candidato para crear oportunidades de crecimiento mutuo. Nuestro enfoque se basa en la integridad, la eficiencia y un profundo conocimiento del mercado laboral. Trabajamos incansablemente para asegurar que cada proceso de selección sea un éxito para todas las partes involucradas, construyendo relaciones duraderas basadas en la confianza y el respeto. Nos enorgullece ser un puente hacia el futuro profesional de miles de personas. Nuestra dedicación se extiende más allá de la simple colocación de un puesto; nos esforzamos por ser un socio estratégico a largo plazo para el crecimiento profesional y empresarial. Nos mantenemos al tanto de las últimas tendencias del mercado para ofrecer soluciones de reclutamiento que anticipen las necesidades futuras de nuestros clientes y candidatos, asegurando que estén siempre a la vanguardia. Cada interacción con nosotros está diseñada para ser una experiencia enriquecedora y de apoyo, proporcionando un valor real y tangible a quienes confían en nuestra expertise.",
        'mision': "Nuestra misión es empoderar a individuos y organizaciones, facilitando la búsqueda del ajuste perfecto entre el talento y las oportunidades laborales. Nos esforzamos por ser el socio estratégico de confianza en el desarrollo de carreras y el crecimiento empresarial, a través de soluciones de reclutamiento personalizadas y de alta calidad. Creemos firmemente que el éxito de una empresa se basa en su capital humano, y nuestra labor es garantizar que ese capital sea de la más alta calidad.",
        'vision': "Aspiramos a ser la principal plataforma de reclutamiento a nivel nacional, reconocida por nuestra innovación, ética y excelencia en el servicio. Buscamos transformar la industria del reclutamiento a través de la tecnología y un enfoque centrado en las personas, creando un ecosistema donde el talento y las oportunidades convergen de manera fluida. Visualizamos un futuro donde cada persona encuentre el trabajo de sus sueños y cada empresa construya el equipo de sus sueños.",
    }
    return render(request, 'app_enzocopto/index.html', context)

def personal(request):
    """
    Vista para la página de personal.
    Pasa una lista de diccionarios con información del personal a la plantilla.
    """
    equipo = [
        {
            'nombre': 'Andrea Salazar',
            'cargo': 'Gerente General',
            'descripcion': 'Lidera la empresa con una visión estratégica y un profundo conocimiento del mercado. Con más de 15 años de experiencia en el sector, Andrea se enfoca en expandir nuestros servicios y mantener la excelencia en cada proyecto. Su compromiso con el desarrollo de talentos es la piedra angular de nuestra filosofía de trabajo. Su liderazgo ha sido fundamental para el crecimiento sostenido de la empresa. Además, es una mentora inspiradora para todo el equipo.',
            'imagen1': 'imagen_1_personal.jpg',
            'imagen2': 'imagen_2_personal.jpg'
        },
        {
            'nombre': 'Marcos Pérez',
            'cargo': 'Director de Operaciones',
            'descripcion': 'Encargado de optimizar los procesos internos y asegurar la eficiencia operativa. Marcos implementa las mejores prácticas para garantizar un servicio ágil y de alta calidad. Su habilidad para resolver problemas y su atención al detalle son clave para el éxito de nuestras operaciones diarias. Ha implementado diversas herramientas tecnológicas que han mejorado significativamente nuestra capacidad de respuesta. Su enfoque pragmático es muy valorado por el equipo.',
            'imagen1': 'imagen_3_personal.jpg',
            'imagen2': 'imagen_4_personal.jpg'
        },
        {
            'nombre': 'Sofía Rojas',
            'cargo': 'Jefa de Reclutamiento',
            'descripcion': 'Experta en identificar y atraer a los mejores candidatos. Sofía tiene un ojo clínico para el talento y una red de contactos inigualable en diversas industrias. Ella lidera nuestro equipo de reclutadores para encontrar a las personas adecuadas para cada vacante. Su pasión por conectar a las personas con las oportunidades correctas es lo que la impulsa a diario. Además, su enfoque humanista en el reclutamiento es muy apreciado por los candidatos.',
            'imagen1': 'imagen_5_personal.jpg',
            'imagen2': 'imagen_6_personal.jpg'
        },
        {
            'nombre': 'Javier Muñoz',
            'cargo': 'Analista de Datos',
            'descripcion': 'Responsable de analizar tendencias del mercado laboral y métricas de reclutamiento. Javier utiliza los datos para optimizar nuestras estrategias y predecir las necesidades futuras de nuestros clientes. Su trabajo asegura que nuestras decisiones se basen en información sólida y actualizada. Su capacidad para transformar datos complejos en información útil es una gran ventaja competitiva. Su enfoque analítico nos ayuda a estar siempre un paso adelante.',
            'imagen1': 'imagen_7_personal.jpg',
            'imagen2': 'imagen_8_personal.jpg'
        },
        {
            'nombre': 'Valeria Soto',
            'cargo': 'Asesora de Carreras',
            'descripcion': 'Guía a los candidatos en su desarrollo profesional, brindando consejos sobre currículums, entrevistas y planes de carrera. Valeria ayuda a los talentos a presentarse de la mejor manera y a alcanzar sus objetivos. Su empatía y conocimiento del mercado son invaluables para quienes buscan un cambio significativo. Su labor es crucial para que nuestros candidatos se sientan preparados y confiados en cada etapa del proceso. Es una figura de apoyo constante.',
            'imagen1': 'imagen_9_personal.jpg',
            'imagen2': 'imagen_10_personal.jpg'
        },
    ]
    context = {'equipo': equipo}
    return render(request, 'app_enzocopto/personal.html', context)

def clientes(request):
    """
    Vista para la página de clientes.
    Pasa una lista de diccionarios con información de los clientes a la plantilla.
    """
    clientes_list = [
        {
            'nombre': 'Empresa A',
            'profesion_oficio': 'Tecnología',
            'reseña': 'Gracias a su equipo de reclutamiento, encontramos a los ingenieros de software que necesitábamos para un proyecto clave. Su proceso fue rápido y eficiente, identificando candidatos que no hubiéramos encontrado por nuestra cuenta. Nos impresionó su profesionalismo y el entendimiento profundo de nuestras necesidades técnicas.',
            'imagen': 'imagen_1_clientes.jpg'
        },
        {
            'nombre': 'Empresa B',
            'profesion_oficio': 'Salud',
            'reseña': 'La calidad de los profesionales de la salud que nos presentaron superó nuestras expectativas. La empresa entendió a la perfección la cultura de nuestra organización y las habilidades específicas que buscábamos. Ahora contamos con un equipo médico de alto rendimiento y estamos muy satisfechos con los resultados. Son un socio de confianza en el sector.',
            'imagen': 'imagen_2_clientes.jpg'
        },
        {
            'nombre': 'Empresa C',
            'profesion_oficio': 'Marketing',
            'reseña': 'Para nuestra última campaña, necesitábamos un equipo de marketing digital con habilidades muy específicas. La empresa nos ayudó a encontrar a los creativos y analistas perfectos que se integraron sin problemas. Su conocimiento del mercado y su capacidad para encontrar el talento adecuado es verdaderamente excepcional. Con ellos, logramos un equipo muy cohesionado.',
            'imagen': 'imagen_3_clientes.jpg'
        },
        {
            'nombre': 'Empresa D',
            'profesion_oficio': 'Finanzas',
            'reseña': 'Buscábamos un perfil muy especializado en finanzas corporativas y su equipo nos presentó a los candidatos más calificados. Su proceso de selección fue riguroso y transparente, lo que nos dio total confianza en su trabajo. Los profesionales que seleccionamos se han adaptado de forma excelente a nuestro entorno. Definitivamente, es una empresa con un gran profesionalismo.',
            'imagen': 'imagen_4_clientes.jpg'
        },
        {
            'nombre': 'Empresa E',
            'profesion_oficio': 'Educación',
            'reseña': 'Para nuestro centro educativo, era vital encontrar educadores con una gran vocación y experiencia. La empresa de reclutamiento nos ayudó a identificar a los candidatos que no solo tenían las credenciales correctas, sino también la pasión por la enseñanza. Estamos muy agradecidos por su dedicación y por ayudarnos a formar un equipo docente de primer nivel.',
            'imagen': 'imagen_5_clientes.jpg'
        },
        {
            'nombre': 'Empresa F',
            'profesion_oficio': 'Retail',
            'reseña': 'Nuestra expansión requería la contratación de personal clave para la gestión de nuevas tiendas. La empresa nos proporcionó un servicio rápido y efectivo, presentándonos a gerentes y supervisores con gran potencial. Su capacidad para manejar un alto volumen de reclutamiento sin sacrificar la calidad es admirable. Son un socio de crecimiento fundamental para nuestro negocio.',
            'imagen': 'imagen_6_clientes.jpg'
        },
        {
            'nombre': 'Empresa G',
            'profesion_oficio': 'Logística',
            'reseña': 'Encontramos a los especialistas en logística que necesitábamos para optimizar nuestra cadena de suministro. Su equipo entendió perfectamente los desafíos de nuestro sector y nos ofreció soluciones de personal que han tenido un impacto directo en nuestra eficiencia. Su expertise en el área es innegable y son un gran apoyo estratégico.',
            'imagen': 'imagen_7_clientes.jpg'
        },
        {
            'nombre': 'Empresa H',
            'profesion_oficio': 'Ingeniería',
            'reseña': 'La empresa nos conectó con ingenieros de proyectos con la experiencia técnica y las habilidades de liderazgo que eran esenciales para nuestro trabajo. El proceso de selección fue meticuloso y los resultados han sido fantásticos. Ahora, nuestros proyectos se ejecutan con mayor fluidez y profesionalismo. Es un gusto trabajar con ellos en cada nuevo proyecto.',
            'imagen': 'imagen_8_clientes.jpg'
        },
        {
            'nombre': 'Empresa I',
            'profesion_oficio': 'Manufactura',
            'reseña': 'Para nuestra planta de producción, necesitábamos personal técnico altamente calificado. La empresa de reclutamiento nos ayudó a encontrar a los operarios y supervisores con la experiencia necesaria para garantizar la calidad. Su servicio fue excepcional y nos permitió cubrir nuestras vacantes de manera eficiente y con gran éxito. Son un aliado en nuestro proceso de producción.',
            'imagen': 'imagen_9_clientes.jpg'
        },
        {
            'nombre': 'Empresa J',
            'profesion_oficio': 'Tecnología',
            'reseña': 'La empresa A se ha convertido en un socio clave para nuestra empresa tecnológica. Siempre nos proporcionan a los mejores ingenieros, diseñadores y gerentes de proyecto. La calidad de los perfiles que nos envían es de un nivel muy alto y nos permiten seguir creciendo. Su rapidez y eficacia es un punto clave para nosotros, ya que siempre se adelantan a nuestras necesidades.',
            'imagen': 'imagen_10_clientes.jpg'
        },
    ]
    context = {'clientes': clientes_list}
    return render(request, 'app_enzocopto/clientes.html', context)

def egresados(request):
    """
    Vista para la página de egresados.
    Pasa una lista de diccionarios con información de los egresados a la plantilla.
    """
    egresados_list = [
        {
            'nombre': 'Juan Gómez',
            'empresa': 'Tech Solutions',
            'opinion': 'Gracias a su asesoría, pude preparar mi currículum y mi entrevista de la mejor manera. Me sentí seguro y listo para enfrentar el proceso de selección. Hoy, gracias a su apoyo, trabajo en una de las empresas de tecnología más innovadoras del país. Su guía fue fundamental para lograr mi primer empleo formal. Siempre les estaré agradecido.',
            'imagen': 'imagen_1_egresados.jpg'
        },
        {
            'nombre': 'Ana Torres',
            'empresa': 'Health Corp',
            'opinion': 'Me ayudaron a encontrar una posición que se ajustaba perfectamente a mis habilidades y mi pasión por el sector salud. Me proporcionaron los contactos y el apoyo necesario para destacar en un mercado competitivo. La empresa se convirtió en mi puente hacia una carrera profesional sólida. Han sido un gran respaldo para mi desarrollo.',
            'imagen': 'imagen_2_egresados.jpg'
        },
        {
            'nombre': 'Pedro Vargas',
            'empresa': 'Marketing Global',
            'opinion': 'El equipo de reclutamiento entendió mi perfil y mis aspiraciones, presentándome a una empresa de marketing donde he podido crecer profesionalmente. Su seguimiento y consejos fueron clave para mi éxito. Recomiendo totalmente su servicio a cualquiera que esté buscando un cambio significativo en su carrera. Tienen un gran ojo para el talento.',
            'imagen': 'imagen_3_egresados.jpg'
        },
        {
            'nombre': 'Claudia Ríos',
            'empresa': 'Financial Group',
            'opinion': 'Como egresada, no sabía por dónde empezar mi búsqueda de empleo. Su servicio me dio la dirección y las herramientas que necesitaba. Hoy, me desempeño en una de las firmas financieras más prestigiosas, algo que no hubiera logrado sin su ayuda. Su apoyo me dio la confianza que necesitaba para triunfar en mi carrera.',
            'imagen': 'imagen_4_egresados.jpg'
        },
        {
            'nombre': 'Felipe Soto',
            'empresa': 'Future Education',
            'opinion': 'Mi paso por el proceso de selección fue mucho más sencillo gracias a la empresa. Me prepararon para la entrevista y me conectaron con la oportunidad ideal. Su dedicación y compromiso con mi éxito profesional me impresionó. Hoy, estoy muy feliz y me siento realizado en mi trabajo como profesor. Ellos me ayudaron a encontrar mi propósito.',
            'imagen': 'imagen_5_egresados.jpg'
        },
        {
            'nombre': 'Rosa Morales',
            'empresa': 'Retail Dynamics',
            'opinion': 'Me proporcionaron una guía clara y consejos prácticos que marcaron la diferencia en mi búsqueda de empleo. Me sentí apoyada en todo momento y el resultado fue una excelente oferta de trabajo en el sector del retail. Su profesionalismo y atención al detalle me hicieron sentir muy especial. Gracias a ellos, pude cumplir mis metas laborales.',
            'imagen': 'imagen_6_egresados.jpg'
        },
        {
            'nombre': 'Luis Castro',
            'empresa': 'Logistics Solutions',
            'opinion': 'El equipo me ayudó a encontrar un puesto que no solo se ajustaba a mi formación, sino que también me ofrecía un camino de crecimiento. Su conocimiento del mercado y su red de contactos son impresionantes. Me siento muy afortunado de haber contado con su apoyo en esta etapa de mi vida profesional. Ellos me impulsaron hacia una carrera brillante.',
            'imagen': 'imagen_7_egresados.jpg'
        },
        {
            'nombre': 'Elena Jiménez',
            'empresa': 'Engineering Corp',
            'opinion': 'Me ayudaron a dar el salto de estudiante a profesional, conectándome con una de las empresas de ingeniería más importantes. Su preparación para la entrevista fue exhaustiva y me dio la confianza necesaria para brillar. Sin su ayuda, este logro no habría sido posible. Me siento muy orgullosa de mi trabajo y de la ayuda que recibí.',
            'imagen': 'imagen_8_egresados.jpg'
        },
    ]
    context = {'egresados': egresados_list}
    return render(request, 'app_enzocopto/egresados.html', context)
