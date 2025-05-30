from app import app, db
from app.models import University, Course

with app.app_context():
    db.drop_all()
    db.create_all()

    # Università
    u1 = University(name="Univerzita Tomáše Bati ve Zlíně")
    u2 = University(name="Universidad Carlos III de Madrid")
    u3 = University(name="Università di Berlino")

    db.session.add_all([u1, u2, u3])
    db.session.commit()

    corsi = [
        # Univerzita Tomáše Bati ve Zlíně
        Course(
            name="Managerial Skills",
            syllabus=(
                "Self-management (techniques applied by changing habits, the fight against procrastination, and self-development). - Time-Management (principles and techniques of time management for setting goals and priorities, tips for work with a diary, techniques for dealing with disturbing and keeping concentration). - Communication, work with papers, an organization of workplace from the view of time management. The role of a secretary from the point of managing the boss's time. - Preparation and managing meetings. - Presentation - a preparation of the presentation and tips of successful speakers. - Dealing with nervousness during a presentation. The use of audio-visual aids by the presentation. - Situational leadership. Mentoring. Coaching. - Delegation. - Giving feedback. - Announcement of unpleasant information. - Techniques used by a problem definition and analysis. - Techniques used by a creative approach to problem-solving. - Techniques used by decision-making."
            ),
            university=u1
        ),

        # Universidad Carlos III de Madrid
        Course(
            name="Propulsion systems performance and design",
            syllabus=(
                "Review of requirements of engine components, the engine design process, the request for proposal, constraint analysis and mission analysis, parametric cycle analysis, turbojet, turbojet with afterburner, turbofan with mixed/unmixed stream, performance cycle analysis, off-design behavior, component matching, installed performances, ramjets and scramjets, sensors, instrumentation and control, control systems requirements and strategy, basic engine control functions, lubrication and cooling, oil systems: lube supply, tank, piping, scavenge system, secondary air system, turbine heat transfer, film cooling, internal cooling (jet impingement, rib-turbulated, pin-fin), bearing and seals, mainshaft bearing types, fatigue life considerations, dynamic seals types (labyrinth seals, carbon seals), structural analysis, fundamentals of rotordynamics, balancing procedures and vibrations suppression, elements of turbomachinery flutter, engine testing and certification."
            ),
            university=u2
        ),
        Course(
            name="Computational Aerodynamics",
            syllabus=(
                "Introduction to Computational Aerodynamics, the mathematical models for fluid flow simulations, the equations of fluid dynamics, the mathematical nature of the flow equations and boundary conditions, discretization techniques, finite difference methods, finite volume methods, structured and unstructured grids, the analysis of numerical schemes, consistency, stability and error analysis, the resolution of numerical schemes, time integration methods, iterative methods for the resolution of algebraic systems, applications to inviscid and/or viscous flows, introduction to turbulence and its modeling, direct numerical simulation (DNS), large eddy simulation (LES), Reynolds-averaged Navier-Stokes (RANS)."
            ),
            university=u2
        )
    ]

    db.session.add_all(corsi)
    db.session.commit()

    print("✅ Database ricreato e popolato con syllabus estesi.")
