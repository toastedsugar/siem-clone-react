import React from "react";

export default function LogItemContainer({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <section className="p-4 bg-zinc-200 dark:bg-zinc-800">
      {children}
    </section>
  );
}
