import React from 'react'
import './NavBarCarrousel.sass'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlus } from '@fortawesome/free-solid-svg-icons'
import _ from 'lodash'

const Carousel = ({ slides, onAddSlide }) => {
  const handleAddSlide = () => {
    onAddSlide()
  }

  return (
    <div className='container-fluid m-0 navbar-carousel-custom-container'>
      <div className='custom_section_navbar_carrusel'>
        {_.map(slides, (slide) => (
          <div key={slide.id} className='custom_section_item_page my-3'>
            <div className='page'>
              <img
                src={slide.image || '/imagenes/white.jpg'}
                alt='Imagen'
                style={{ width: '30px', height: '30px', marginRight: '1px' }}
              />
              {slide.id}
            </div>
          </div>
        ))}
        <button
          className='custom-navbar-carrousel-button'
          onClick={handleAddSlide}
        >
          <FontAwesomeIcon icon={faPlus} />
        </button>
      </div>
    </div>
  )
}

export default Carousel
