# AgriAid Design System

## 🎨 Color Palette

### Primary Colors

- **Primary Dark**: `#1b4332` - Deep forest green (headers, important elements)
- **Primary**: `#2d6a4f` - Rich green (main brand color)
- **Secondary**: `#40916c` - Medium green (secondary actions)
- **Accent**: `#52b788` - Light green (highlights, hover states)
- **Light Green**: `#95d5b2` - Soft green (subtle accents)

### Background Colors

- **Light Background**: `#d8f3dc` - Very light green
- **Lighter Background**: `#b7e4c7` - Pale green
- **White**: `#ffffff` - Pure white (cards, content areas)

### Text Colors

- **Dark Text**: `#1b4332` - Primary text
- **Gray Text**: `#6b7280` - Secondary text

### UI Elements

- **Border**: `#e5e7eb` - Light gray borders
- **Shadows**: Multiple levels of shadows with green tints

## 🎯 Typography

### Font Family

- Primary: `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif`
- Fallback: System fonts

### Font Weights

- Regular: `400`
- Medium: `500`
- Semibold: `600`
- Bold: `700`

### Font Sizes

- Heading 1: `3.5rem` (56px)
- Heading 2: `2.5rem` (40px)
- Heading 3: `2rem` (32px)
- Body: `1rem` (16px)
- Small: `0.875rem` (14px)

## 🧩 Components

### Buttons

#### Primary Button

```css
background: linear-gradient(135deg, #1b4332 0%, #2d6a4f 100%);
color: white;
padding: 12px 28px;
border-radius: 10px;
font-weight: 600;
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
transition: all 0.3s ease;
```

Hover: `transform: translateY(-2px); box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);`

#### Secondary Button

```css
background: linear-gradient(135deg, #40916c 0%, #52b788 100%);
/* Same styling as primary */
```

### Cards

#### Standard Card

```css
background: white;
border-radius: 16px;
border: 2px solid #e5e7eb;
padding: 24px;
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
transition: all 0.3s ease;
```

Hover: `transform: translateY(-8px); border-color: #40916c; box-shadow: 0 12px 24px rgba(45, 106, 79, 0.15);`

### Sidebar

#### Navigation Sidebar

```css
width: 260px;
background: linear-gradient(180deg, #1b4332 0%, #2d6a4f 100%);
padding: 30px 20px;
box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
```

#### Sidebar Links

```css
color: white;
padding: 12px 15px;
border-radius: 8px;
transition: all 0.3s ease;
```

Hover: `background: rgba(255, 255, 255, 0.1); color: #95d5b2; transform: translateX(5px);`

### Form Elements

#### Input Fields

```css
width: 100%;
padding: 12px 16px;
border: 1px solid #e5e7eb;
border-radius: 8px;
transition: all 0.3s ease;
```

Focus: `border-color: #40916c; box-shadow: 0 0 0 3px rgba(64, 145, 108, 0.1); transform: translateY(-2px);`

### Drop Zone (File Upload)

```css
border: 3px dashed rgba(255, 255, 255, 0.6);
border-radius: 24px;
width: 400px;
height: 280px;
background: rgba(255, 255, 255, 0.15);
backdrop-filter: blur(10px);
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
```

Hover: `background: rgba(255, 255, 255, 0.25); border-color: white; transform: translateY(-5px);`

## 🎬 Animations

### Gradient Animation

```css
@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
```

Used on hero backgrounds with `background-size: 400% 400%` and `animation: gradient 15s ease infinite`

### Fade In

```css
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### Hover Transitions

All interactive elements use `transition: all 0.3s ease` for smooth state changes.

## 📐 Spacing System

- **Extra Small**: `8px`
- **Small**: `12px`
- **Medium**: `16px`
- **Large**: `24px`
- **Extra Large**: `32px`
- **XXL**: `40px`

## 🌓 Shadow System

```css
--shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.08);
--shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 8px 24px rgba(45, 106, 79, 0.2);
--shadow-xl: 0 12px 40px rgba(45, 106, 79, 0.25);
```

## 📱 Responsive Breakpoints

- **Mobile**: `< 768px`
- **Tablet**: `768px - 1024px`
- **Desktop**: `> 1024px`

## 🎨 Design Principles

1. **Consistency**: Use the same components and patterns across all pages
2. **Hierarchy**: Clear visual hierarchy with proper spacing and typography
3. **Feedback**: Immediate visual feedback on all interactions
4. **Accessibility**: High contrast ratios and keyboard navigation
5. **Performance**: Smooth animations (60fps) and quick load times
6. **Modern**: Glassmorphism, gradients, and contemporary UI patterns

## 🚀 Implementation Notes

- All transitions are 0.3s for consistency
- Hover states include both color changes AND transforms for depth
- Gradient backgrounds use multiple colors for visual richness
- Cards lift on hover with increased shadows for 3D effect
- Icons from Bootstrap Icons and Lineicons for consistency
- Tailwind CSS utility classes used where appropriate
- Custom CSS for unique components and animations

## 📦 Dependencies

- **Tailwind CSS**: For utility classes and responsive design
- **Bootstrap Icons**: For consistent iconography
- **GSAP**: For advanced animations (falling leaves effect)
- **Font Awesome**: Additional icons on home page

---

_Last Updated: November 1, 2025_
