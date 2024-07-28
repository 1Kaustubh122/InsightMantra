import { curve, heroBackground, robot } from "../assets";
import Button from "./Button";
import Section from "./Section";
import { BackgroundCircles, BottomLine, Gradient } from "./design/Hero";
import { useRef } from "react";
<<<<<<< HEAD
import Generating from "./Generating";
=======
>>>>>>> e5fc04402ff72ca0d6b0572002513afe7ef9f86e
import CompanyLogos from "./CompanyLogos";

const Hero = () => {
  const parallaxRef = useRef(null);

  return (
    <Section
      className="pt-[12rem] -mt-[5.25rem]"
      crosses
      crossesOffset="lg:translate-y-[5.25rem]"
      customPaddings
      id="hero"
    >
      <div className="container relative" ref={parallaxRef}>
        <div className="relative z-1 max-w-[62rem] mx-auto text-center mb-[3.875rem] md:mb-20 lg:mb-[6.25rem]">
<<<<<<< HEAD
          <h1 className="h1 mb-6">
            Explore the Possibilities &nbsp;In&nbsp;Demand {` `}
=======
        
          <h1 className="h1 mb-2 text-6xl md:text-6xl lg:text-8xl">
          <span className="inline-block whitespace-nowrap ml-[-2rem] md:ml-[-3rem] lg:ml-[-4rem]"> Explore the Possibilities </span> &nbsp;In&nbsp;Demand {` `}
>>>>>>> e5fc04402ff72ca0d6b0572002513afe7ef9f86e
            <span className="inline-block relative">
              Forcasting {" "}
              <img
                src={curve}
                className="absolute top-full left-0 w-full xl:-mt-2"
                width={624}
                height={28}
                alt="Curve"
              />
            </span>
          </h1>
<<<<<<< HEAD
          <p className="body-1 max-w-3xl mx-auto mb-6 text-n-2 lg:mb-8">
            Forcast Demand Manufacture
          </p>
          <Button href="/pricing" white>
            Get started
          </Button>
        </div>
        <div className="relative max-w-[23rem] mx-auto md:max-w-5xl xl:mb-24">
          <div className="relative z-1 p-0.5 rounded-2xl bg-conic-gradient">
            <div className="relative bg-n-8 rounded-[1rem]">
              <div className="h-[1.4rem] bg-n-10 rounded-t-[0.9rem]" />

              <div className="aspect-[33/40] rounded-b-[0.9rem] overflow-hidden md:aspect-[688/490] lg:aspect-[1024/490]">
                <img
                  src={robot}
                  className="w-full scale-[1.7] translate-y-[8%] md:scale-[1] md:-translate-y-[10%] lg:-translate-y-[15%]"
                  width={1024}
                  height={490}
                  alt="AI"
                />

                <Generating className="absolute left-4 right-4 bottom-5 md:left-1/2 md:right-auto md:bottom-8 md:w-[30rem] md:-translate-x-1/2" />

                <ScrollParallax isAbsolutelyPositioned>
                  <ul className="hidden absolute -left-[5.5rem] bottom-[7.5rem] px-1 py-1 bg-n-9/40 backdrop-blur border border-n-1/10 rounded-2xl xl:flex">
                    {heroIcons.map((icon, index) => (
                      <li className="p-5" key={index}>
                        <img src={icon} width={24} height={25} alt={icon} />
                      </li>
                    ))}
                  </ul>
                </ScrollParallax>

                
              </div>
            </div>

            <Gradient />
=======
          <p className="body-1 max-w-3xl mx-auto mt-4 mb-6 text-n-2 lg:mt-6 lg:mb-8">
            Forcast-Demand-Manufacture
          </p>
          <Button
  className="mt-4 lg:mt-6 text-lg lg:text-xl px-6 lg:px-8 py-3 lg:py-4 bg-cyan-500 hover:bg-transparent transition duration-300 relative border-0 rounded-lg overflow-hidden"
  style={{
    borderRadius: '30px 50px 0 0',
  }}
  href="/pricing"
>
  <span className="text-black hover:text-white transition duration-300">
    Get Started Today
  </span>
</Button>
   
>>>>>>> e5fc04402ff72ca0d6b0572002513afe7ef9f86e
          </div>
        <div className="relative max-w-[23rem] mx-auto md:max-w-5xl xl:mb-24">
          
          <div className="absolute -top-[54%] left-1/2 w-[234%] -translate-x-1/2 md:-top-[46%] md:w-[138%] lg:-top-[104%]">
            <img
              src={heroBackground}
              className="w-full"
              width={1440}
              height={1800}
              alt="hero"
            />
          </div>

          <BackgroundCircles />
        </div>

        
      </div>

      <BottomLine />
    </Section>
  );
};

export default Hero;
